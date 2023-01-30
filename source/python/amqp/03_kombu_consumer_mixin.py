# ConsumerMixin will create a robust consumer out of the box. Robust consumer
# means, it quickly recovers from failures.

from kombu.mixins import ConsumerMixin
from kombu import Connection, Exchange, Queue

rabbit_url = "amqp://localhost:5672/"

# We need to create a class that inherits from ConsumerMixin
# The ConsumerMixin class expects the descendant class to have an attribute 
# of connection, which is an instance of the kombu Connection class.
class Worker(ConsumerMixin):
    def __init__(self, connection, queues):
        self.connection = connection
        self.queues = queues
    # We need to specify the function that will get called when a Consumer
    # receives a message. 
    def on_message(self, body, message):
        print('Got message: {0}'.format(body))
        message.ack()
        
    # Another responsibility of the descendant class is to implement the
    # get_consumers function, which returns a list of the Consumers the worker
    # will use. Each consumer is an instance of the kombu Consumer class
    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=self.queues, callbacks=[self.on_message])]
    
exchange = Exchange("MyExchange", type="direct")
queue_a = Queue(name="queue-A", exchange=exchange, routing_key="AAA")
queue_b = Queue(name="queue-B", exchange=exchange, routing_key="BBB") 
queues = [queue_a, queue_b]

'''
[2023-01-30 16:35:52]: doc/sphinx-doc  (git)-[main]-$ rabbitmqctl list_queues
Timeout: 60.0 seconds ...
Listing queues for vhost / ...
name	messages
queue-B	0
queue-A	11
'''

with Connection(rabbit_url, heartbeat=4) as conn:
    worker = Worker(conn, queues)
    worker.run() # ConsumerMixin supplies run

# - The run function loops continuously until an error occurs or the process is terminated.
# - During it’s looping it consumes messages from the queues supplied and calls the on_message function for each message.
# - It also repeatedly calls the heartbeat_check function to ensure the connection to RabbitMQ is good, and if it is not good it recovers the connection and continues consuming.

'''
>>> with Connection(rabbit_url, heartbeat=4) as conn:
...     worker = Worker(conn, queues)
...     worker.run() # ConsumerMixin supplies run
... 
Got message: Hi Mr.AAA!
Got message: Hello Mr.AAA!
Got message: Hello Mr.AAA!
Got message: Hello Mr.AAA!
Got message: Hi Mr.AAABB!
Got message: Hi Mr.AAA!
Got message: Hi Mr.AAABB!
Got message: Hi Mr.AAABB!
Got message: Hi Mr.AAABB!
Got message: Hi Mr.AAABB!
Got message: Hi Mr.Ajeeb!

[2023-01-30 16:36:19]: doc/sphinx-doc  (git)-[main]-$ rabbitmqctl list_queues
Timeout: 60.0 seconds ...
Listing queues for vhost / ...
name	messages
queue-B	0
queue-A	0


In another terminal

>>> producer_a.publish("Hi Mr.Ajeeb!")
<promise@0x10d45eb00>
>>> producer_b.publish("Hi Mr.Ajeeb!")
<promise@0x10d45eb90>


Got message: Hi Mr.Ajeeb!
Got message: Hi Mr.Ajeeb!

'''