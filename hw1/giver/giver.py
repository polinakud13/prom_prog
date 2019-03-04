import pika
import random
import time
import sys

while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
        channel = connection.channel()
        
        channel.queue_declare(queue='hello')
        while True:
            sleep_time = random.uniform(0.5,3)
            time.sleep(sleep_time)
            sending = random.randint(1,57)
            channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=str(sending))
            print("Sent %d after %.2f time"%(sending,sleep_time))
    except (pika.exceptions.ConnectionClosed, OSError):
        print('Connect again', file=sys.stderr, flush=True)
        time.sleep(1)
connection.close()