import pika, sys, os


def main():
    # Establish a connection with RabbitMQ server which runs on docker container
    # The connection is established with the default port 5672
    # BlockingConnection is used to block the connection until the connection is established
    # ConnectionParameters is used to pass the host name of the RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

    # Create a channel
    # a channel is a virtual connection inside a connection, you can think it as thread inside a connection
    channel = connection.channel()

    # Declare a queue
    # if the queue is not present, it will be created
    # if the queue is present, it will not be created
    channel.queue_declare(queue="chat")

    # Define a callback function to print the message
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    # Publish a message to the queue
    # the message is a string
    channel.basic_consume(queue="chat", on_message_callback=callback, auto_ack=True)

    # Start consuming the messages
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
