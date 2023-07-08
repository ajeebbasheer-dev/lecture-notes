from kombu import Connection, Exchange, Producer, Queue, Consumer

# To establish a connection to a RabbitMQ server, Kombu uses a Connection class.

rabbit_url = "amqp://localhost:5672/"
conn = Connection(rabbit_url)

# Using that connection we need to create a channel. It is the channel that is
# used when sending messages:

channel = conn.channel()

# Specify the exchange
exchange = Exchange("MyExchange", type="direct")

# Create 2 queues
queue_a = Queue(name="queue-A", exchange=exchange, routing_key="AAA")
queue_b = Queue(name="queue-B", exchange=exchange, routing_key="BBB") 

# bind the queues to the exchange.
queue_a.maybe_bind(conn)
queue_a.declare() # create the queue

queue_b.maybe_bind(conn)
queue_b.declare() # create the queue

# We then need to create a producer. Kombu has the Producer class for this
producer_a = Producer(exchange=exchange, channel=channel, routing_key="AAA")
producer_b = Producer(exchange=exchange, channel=channel, routing_key="BBB")

# it's time to send a message.

producer_a.publish("Hi Mr.AAA!")
producer_a.publish("Hello Mr.AAA!")

producer_b.publish("Hello Mr.BBB!")

'''
--- RUN `rabbitmqctl list_queues` ---

[2023-01-30 15:00:50]: doc/sphinx-doc  (git)-[main]-$ rabbitmqctl list_queues
Timeout: 60.0 seconds ...
Listing queues for vhost / ...
name	messages
queue-B	1
queue-A	2
'''

## Consumer

def process_message(body, message):
    print(f"The body is {body}")
    message.ack()


# The drain_events function will wait for 2 seconds for the consumers to 
# consume a message and error with a timeout error if the queue is empty.
# drain_events will drain events from all channels on a connection.
with Consumer(conn, queues=queue_a, callbacks=[process_message], accept=["text/plain"]):
    conn.drain_events(timeout=2) # Without the timeout argument, it indefinitely waits for a message

'''
>>> with Consumer(conn, queues=queue_a, callbacks=[process_message], accept=["text/plain"]):
...     conn.drain_events(timeout=2)
... 
The body is Hi Mr.AAA!
The body is Hello Mr.AAA!
'''


'''
We can see the Queue-A is empty now as all it's messages are consumed.

[2023-01-30 15:04:03]: doc/sphinx-doc  (git)-[main]-$ rabbitmqctl list_queues
Timeout: 60.0 seconds ...
Listing queues for vhost / ...
name	messages
queue-B	1
queue-A	0
'''

with Consumer(conn, queues=queue_b, callbacks=[process_message], accept=["text/plain"]):
    conn.drain_events(timeout=2)

'''
>>> with Consumer(conn, queues=queue_b, callbacks=[process_message], accept=["text/plain"]):
...     conn.drain_events(timeout=2)
... 
The body is Hello Mr.BBB!

[2023-01-30 15:04:58]: doc/sphinx-doc  (git)-[main]-$ rabbitmqctl list_queues
Timeout: 60.0 seconds ...
Listing queues for vhost / ...
name	messages
queue-B	0
queue-A	0
'''


'''
consumer = Consumer(conn, queues=queue_b, callbacks=[process_message], accept=["text/plain"])
consumer.consume() # consumer ready to go.
conn.drain_events(timeout=2) # actually triggers the consuming.

'''
