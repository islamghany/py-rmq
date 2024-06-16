import pika, random, time

# Create the connection
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# Create the channel
channel = connection.channel()

# create the direct exchange
channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

# logs severity levels
severities = ["info", "warning", "error", "debug"]
messages = ["EMsg", "WMsg", "ErrMsg", "DMsg"]

for i in range(10):
    randomNum = random.randint(0, 3)
    msg = messages[randomNum]
    severity = severities[randomNum]
    channel.basic_publish(exchange="direct_logs", routing_key=severity, body=msg)
    print(f" [x] Sent {severity}: {msg}")
    time.sleep(1)

channel.exchange_delete(exchange="direct_logs", if_unused=False)

# Close the connection
connection.close()
