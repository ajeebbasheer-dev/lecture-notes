=========
RabbitMQ
=========

- Based on Advance Message Queuing Protocol (**AMQP**).
- High-level flow:

    - 1. An application (PRODUCER) sends a message to a RabbitMQ server.
    - RabbitMQ server routes that message to a queue.
    - Another application (CONSUMER) listening to that queue receives that message and does whatever it needs to with it

- **Post Office Analogy**: RabbitMQ is a post box, a post office, and a letter carrier.
- **Exchange** within RabbitMQ does the routing.

    - Producer tells the RabbitMQ server which Exchange it want to use.
    - Exchange decides which queue to put the message on.

- How does an exchange know which queue(s) to route the message to? There are 3 types of exchanges:

    - **direct**: When a queue is declared (created) it is bound to the exchange with a routing key. When a producer sends a message it sends a routing key with it. The exchange takes the routing key of the message and matches it the routing keys of the queues bound to it. If it matches multiple queue’s routing keys, then the messages gets added to them all.
    - **fanout**:
    - **topic**:

- A consumer must specify with queue it is listening to.


The rabbitmqctl Command
=========================

If you have installed rabbitmq using Homebrew (MAC), then export the path::

    export PATH=$PATH:/usr/local/opt/rabbitmq/sbin


Kombu
======

Note: Understand `01_kombu_basics.py` code before proceeding.
**03_kombu_consumer_mixin.py** is the reliable & robust consumer code.

From the example, we know that to consume as soon as producer produce a message::

    import socket
    while True:
      try:
        conn.drain_events(timeout=2)
      except socket.timeout:
        pass # This will do for now

What happens if there is a connection failure??

Kombu Connection class provides:

- clone():  creates a copy of the connection with the same connection settings.
- ensure_connection(): makes sure the connection is good or errors

Using these, we can revive a connection::

    def establish_connection():
        revived_connection = conn.clone()
        revived_connection.ensure_connection(max_retries=3)
        channel = revived_connection.channel()
        consumer.revive(channel)
        consumer.consume()
        print("connection revived!")
        return revived_connection

and use a robust function to consume ::

    def consume():
        new_conn = establish_connection()
        while True:
            try:
                new_conn.drain_events(timeout=2)
            except socket.timeout:
                pass # This will do for now

this will revive connection failures and continues consuming::

    def run():
        while True:
            try:
                consume()
            except conn.connection_errors:
                pass


This increases the robustness of the consumer **but we can do better! (03_kombu_consumer_mixin.py)**


heartbeats
------------


- **Currently, it can take quite some time to detect that a connection is dead and to enable speedy detection there is the concept of heartbeats in AMQP. This is a quote from the RabbitMQ documentation:**
- **heartbeat is a message from application (our consumer) to the server (rabbit server) and vice versa to signal that the connection is still good.**

::

    conn = Connection(rabbit_url, heartbeat=10)
    # we now need to call the function heartbeat_check at least twice as often on the connection

    # consume function will become.
    def consume():
        new_conn = establish_connection()
        while True:
            try:
                new_conn.drain_events(timeout=2)
            except socket.timeout:
                new_conn.heartbeat_check()

Message Expiration
---------------------

Default expiration for a published message is 30 minutes.

We can change that using **expiration** argument in a publish() function.

Let's publish couple of messages::

    producer_a.publish("Hi Mr. Adam")
    producer_b.publish("Hi Mr. Bob")
    producer_a.publish("OTP = 12432", expiration=20)
    producer_b.publish("OTP = 32412", expiration=60)

On another terminal::

    with Connection(rabbit_url, heartbeat=4) as conn:
        time.sleep(25)
        worker = Worker(conn, queues)
        worker.run() 

Can see the 3rd message got expired after 20 seconds::

    >>> with Connection(rabbit_url, heartbeat=4) as conn:
    ...     time.sleep(25)
    ...     worker = Worker(conn, queues)
    ...     worker.run() 
    ... 
    Got message: Hi Mr. Adam
    Got message: Hi Mr. Bob
    Got message: OTP = 32412

