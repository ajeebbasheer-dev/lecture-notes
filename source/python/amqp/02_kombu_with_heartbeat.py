from kombu import Connection, Exchange, Producer, Queue, Consumer
import socket

conn = Connection("amqp://localhost:5672/", heartbeat=10)

channel = conn.channel()
exchange = Exchange("MyExchange", type="direct")
queue_a = Queue(name="queue-A", exchange=exchange, routing_key="AAA")
queue_a.maybe_bind(conn)
queue_a.declare()

producer_a = Producer(exchange=exchange, channel=channel, routing_key="AAA")
producer_a.publish("Hi Mr.AAA!")
producer_a.publish("Hello Mr.AAA!")

consumer = Consumer(conn, queues=queue_a, callbacks=[process_message], accept=["text/plain"])
consumer.consume() # ready to consume

# This logic is explained in the documentation.
def establish_connection():
    revived_connection = conn.clone()
    revived_connection.ensure_connection(max_retries=3)
    channel = revived_connection.channel()
    consumer.revive(channel)
    consumer.consume()
    return revived_connection

def consume():
    new_conn = establish_connection()
    while True:
        try:
            new_conn.drain_events(timeout=2)
        except socket.timeout:
            new_conn.heartbeat_check()

def run():
    while True:
        try:
            consume()
        except conn.connection_errors:
            print("connection revived")

run()

# In another terminal produce message to this queue (queue-a)