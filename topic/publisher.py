import pika, random, time

# Establish a connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# Create a channel
channel = connection.channel()

# Declare a topic exchange
channel.exchange_declare(exchange="topic_logs", exchange_type="topic")


serverities = ["info", "warning", "error"]
priorities = ["high", "medium", "low"]

# Generate a random message
for i in range(10):
    random_severity = random.choice(serverities)
    random_priority = random.choice(priorities)
    message = f"{random_severity} {random_priority} message"
    routing_key = f"{random_severity}.{random_priority}"
    channel.basic_publish(exchange="topic_logs", routing_key=routing_key, body=message)
    print(f"Sent: {routing_key} - {message}")
    time.sleep(1)

channel.exchange_delete(exchange="topic_logs", if_unused=False)

connection.close()
