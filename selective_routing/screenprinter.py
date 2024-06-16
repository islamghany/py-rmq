import pika

severities = ["info", "warning", "error", "debug"]
errorRK = severities[2]
warningRK = severities[1]
infoRK = severities[0]
debugRK = severities[3]

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
channel.queue_bind(exchange="direct_logs", queue=queue_name, routing_key=errorRK)
channel.queue_bind(exchange="direct_logs", queue=queue_name, routing_key=warningRK)
channel.queue_bind(exchange="direct_logs", queue=queue_name, routing_key=infoRK)
channel.queue_bind(exchange="direct_logs", queue=queue_name, routing_key=debugRK)

print(" [*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(f" [x] screen printer received {method.routing_key}: {body}")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
