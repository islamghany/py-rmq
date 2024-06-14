This is a Python program that interacts with the RabbitMQ message broker

## 1. start the RabbitMQ server

```bash
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```

## 2. install the required packages

```bash
pip install pika
```

## 3. run the program

```bash
python3 publisher.py
```

```bash
python3 consumer.py
```

## 4. stop the RabbitMQ server

```bash
docker stop rabbitmq
```

```bash
docker rm rabbitmq
```
