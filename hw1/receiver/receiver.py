import pika
import os
import sys
import time
params = pika.URLParameters(os.getenv('RABBITMQ_URL'))



def callback(ch, method, properties, number):
    print("Received %d" % int(number))

while True:
    try:
        connection = pika.BlockingConnection(params)
        channel = connection.channel()  
        channel.queue_declare(queue='hello')
        channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
        channel.start_consuming()
    except (pika.exceptions.ConnectionClosed, OSError):
        print('Connect again', file=sys.stderr, flush=True)
        time.sleep(1)
