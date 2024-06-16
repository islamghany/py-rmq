import pika

severities = ["info", "warning", "error", "debug"]
warningRK = severities[1]

# Create the connection
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# Create the channel
channel = connection.channel()

# create the direct exchange if not exist
channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

# create the queue to bind it to the exchange
result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

# bind the queue to the exchange
channel.queue_bind(exchange="direct_logs", queue=queue_name, routing_key=warningRK)

print(" [*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(f" [x] writing file Received: {method.routing_key}: {body}")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
