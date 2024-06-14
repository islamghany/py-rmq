import pika

connection = None


def main():
    # Establish a connection with RabbitMQ server which runs on docker container
    # The connection is established with the default port 5672
    # BlockingConnection is used to block the connection until the connection is established
    # ConnectionParameters is used to pass the host name of the RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

    # Create a channel
    # a channel is a virtual connection inside a connection, you can think it as thread inside a connection
    channel = connection.channel()

    # Optional: create an exchange and specify the the bingings

    # Declare a queue
    # if the queue is not present, it will be created
    # if the queue is present, it will not be created
    channel.queue_declare(queue="chat")

    # start reading from the standard input
    while True:
        message = input("Enter the message: ")
        if message == "exit":
            break
        # Publish a message to the queue
        # the message is a string
        channel.basic_publish(exchange="", routing_key="chat", body=message)
        print(f" [x] Sent {message}")

    # Close the connection
    connection.close()


if __name__ == "__main__":
    main()
