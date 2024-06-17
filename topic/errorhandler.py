# error will handle all the errors
import pika

# Establish a connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# Create a channel
channel = connection.channel()

# Declare a topic exchange
channel.exchange_declare(exchange="topic_logs", exchange_type="topic")

# Declare a queue
result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

# Bind the queue to the exchange
channel.queue_bind(exchange="topic_logs", queue=queue_name, routing_key="error.#")


def error_handler(ch, method, properties, body):
    print(f"Error Received: {method.routing_key} - {body}")


# Consume the queue
channel.basic_consume(
    queue=queue_name, on_message_callback=error_handler, auto_ack=True
)

# Start consuming
channel.start_consuming()
