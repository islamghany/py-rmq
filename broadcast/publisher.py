import pika, time

# Create the connection
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# Create the channel
channel = connection.channel()

# create the fanout exchange
channel.exchange_declare(exchange="logs", exchange_type="fanout")

for i in range(10):
    # Publish a message to the exchange
    # the message is a string
    channel.basic_publish(exchange="logs", routing_key="", body=f"Hello World {i}")
    print(f" [x] Sent Hello World {i}")
    # sleep for 1 second
    time.sleep(1)

# delete the exchange even if it is in use by the queue
channel.exchange_delete(exchange="logs", if_unused=False)

# Close the connection
channel.close()
