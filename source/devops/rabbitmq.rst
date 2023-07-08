==========
RabbitMQ
==========

- **AMQP**: Starndardizes messaging using **producers**, **broker** and **consumers**.
- **Messaging**: increases loose coupling and scalability.

RabbitMQ is a open source messaging broker that implements AMQP.



- **Pubilsh** means producer adding a message to the **Exchange**.
- **Exchange** is binded with multiple **queues** with a **binding key**.
- Exchange compares **routing key** with this binding key.
- Message distribution depends on exchange type.

    - **default**: created by rabbitmq. compares routing key with queue name. Indirectly allows sending directly to the queues.
    - 

https://www.rabbitmq.com/


Docker installation
====================

- https://hub.docker.com/_/rabbitmq
- rabbitmq listens on 5672
- rabbitmq management gui listens on 15672 with default username-password `guest-guest`

::

    docker run -it --rm --name rabbitmq -p5672:5672 -p15672:15672 rabbitmq:3.11-management

To set username and password::

    -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=pw


We have binded management app with 15672.

.. image:: images/rabbitmq/mgmt_gui.png
    :width: 600
    :align: center

Hands-on (Kombu)
==================

Messaging Scenarios
---------------------

1. **Request/Reply**: Works like the postal service.  A message is addressed to a single recipient, with a return address printed on the back. The recipient may or may not reply to the message.
    - achieved using **direct exchanges**.
2. **Broadcast**: message is sent to all parties.
    - achieved using **fanout exchanges**
3. **Publish/Subscribe**:  Producers publish messages to topics, and consumers subscribe to the topics they are interested in.
    - achieved using **topic exchanges**.

Reliability
------------

AMQP defines two built-in delivery modes:

1. persistent: Messages are written to disk and **survives a broker restart**.
2. transient (**fastest**): Messages may or may not be written to disk, as the broker sees fit to optimize memory contents. The messages won’t survive a broker restart.

Simple Example
---------------

::

    >>> from kombu import Connection, Exchange, Queue
    >>> conn = Connection('amqp://guest:guest@localhost:5672//')
    >>> conn
    <Connection: amqp://guest:**@localhost:5672// at 0x7f03512edc50>
    >>> conn.connect()
    <AMQP Connection: 127.0.0.1:5672// using <TCPTransport: 127.0.0.1:39912 -> 127.0.0.1:5672 at 0x7f034300d2f0> at 0x7f0343032048>
    >>> conn.connected
    True

.. image:: images/rabbitmq/conn.png
    :width: 200
    :align: center

Create exchange and queue::

    >>> my_ex = Exchange('my_ex', 'topic')
    >>> my_queue = Queue('my_queue', exchange=my_ex, routing_key='hello')
    >>> producer = conn.Producer(serializer='json')

Try to publish a message::

    >>> producer.publish({'hello': 'john'}, exchange=my_ex, routing_key="hello")
    <promise@0x7f034303baf8>

ERROR! (no exchange 'my_ex')::

    2023-06-26 17:11:07.439295+00:00 [error] <0.4645.0> operation basic.publish caused a channel exception not_found: no exchange 'my_ex' in vhost '/'

