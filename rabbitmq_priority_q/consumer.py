import time
import pika

if __name__=="__main__":

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    channel = connection.channel()

    channel.queue_declare(queue='hello', arguments={"x-max-priority": 10})

    while True:

        method_frame, header_frame, body = channel.basic_get('hello')
        if method_frame:
            channel.basic_ack(method_frame.delivery_tag)
            print("Recieved :", body)
        time.sleep(0.1)


# Tutorial followed : https://github.com/hardiksondagar/rabbitmq-priority-queue-example