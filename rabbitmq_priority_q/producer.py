#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

channel.queue_declare(queue='hello', arguments={"x-max-priority": 10})
priority= int(sys.argv[1]) if len(sys.argv) > 1 else 0

for i in range(5):

    message = f"message#{i+1}-with-priority-{priority}"
    channel.basic_publish(exchange='', routing_key='hello', body=message, properties=pika.BasicProperties(priority=priority))
    print(" [x] Sent 'Hello World!'")
connection.close()