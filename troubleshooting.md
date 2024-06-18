# Failure Points in RabbitMQ

## Publisher Connection/Channel Failure

When a publisher trying to publish a message to RabbitMQ, it can fail due to the following reasons:

1. **Connection Failure**: Publisher can fail to establish a connection with RabbitMQ server. This can happen due to network issues, RabbitMQ server is down, or the publisher is not able to connect to the RabbitMQ server.
2. **Channel Failure**: Publisher can fail to create a channel to RabbitMQ server. This can happen due to network issues, RabbitMQ server is down, or the publisher is not able to create a channel to the RabbitMQ server.

One Way to ensure that the message is delivered to RabbitMQ is to ask the channel to confirm the message delivery. This can be done by setting the `confirm` property to `true` while creating the channel.

```python
channel.confirm_delivery()
```

and when publishing the message, wait for the confirmation from the channel.

```python
try:
    channel.basic_publish(
        exchange='',
        routing_key='queue_name',
        body='Hello World',
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        )
    )
    print("Message Published")
except pika.exceptions.ChannelClosed as e:
    print("Channel Closed")
except pika.exceptions.ConnectionClosed as e:
    print("Connection Closed")
```

Like that we can ensure that the message is delivered to RabbitMQ server or not.

## 2. Exchange/Queue Failure

When a publisher sends a message to RabbitMQ, it is first sent to an exchange. The exchange then routes the message to the appropriate queue. If the exchange or queue is down or restarted, the message will not be delivered to the queue.

To ensure that the message is delivered to the queue, we can declare the exchange and queue as durable. This will ensure that the exchange and queue are persistent and will not be lost even if the RabbitMQ server is restarted.

```python
channel.exchange_declare(
    exchange='exchange_name',
    exchange_type='direct',
    durable=True
)

channel.queue_declare(
    queue='queue_name',
    durable=True
)
```

By declaring the exchange and queue as durable, we can ensure that the message is delivered to the queue even if the exchange or queue is down or restarted.

## 3. Consumer Failure

When a consumer tries to consume a message from RabbitMQ, the consumer has automatically/manual ack mode. If the consumer is in automatic ack mode and the consumer fails to process the message, the message will be lost.

To ensure that the message is not lost, we can set the consumer to manual ack mode and acknowledge the message only after the message is processed successfully.

```python

def callback(ch, method, properties, body):
    try:
        # Process the message
        print("Message Processed")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print("Error Processing Message")
        # Requeue the message
        ch.basic_nack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    queue='queue_name',
    on_message_callback=callback,
    auto_ack=False
)
```

Another problem that may occur that the consumer is overloaded with messages and is not able to process the messages in time. This can lead to a backlog of messages in the queue and the consumer may not be able to process all the messages.

To handle this situation, we can set the `prefetch_count` property to limit the number of unacknowledged messages that the consumer can handle at a time.

```python
channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    queue='queue_name',
    on_message_callback=callback,
    auto_ack=False
)
```
