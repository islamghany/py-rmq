import pika

# Create the connection
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# Create the channel
channel = connection.channel()

# create the fanout exchange (willnot affect if already exists)
channel.exchange_declare(exchange="logs", exchange_type="fanout")

# declare the queue, the queue is exclusive
# we can declare the queue with the empty name, the server will create a unique queue name
# and when the connection is closed, the queue will be deleted
result = channel.queue_declare(queue="", exclusive=True)

# bind the queue with the exchange
queue_name = result.method.queue
print("subscribe to queue: ", queue_name)
channel.queue_bind(exchange="logs", queue=queue_name)


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


print(" [*] Waiting for logs. To exit press CTRL+C")

# start consuming the messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
