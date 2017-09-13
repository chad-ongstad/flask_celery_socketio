from celery import Celery
import time
from flask_socketio import SocketIO


celery=Celery('demo',broker='amqp://')

socketio = SocketIO(message_queue='amqp:///socketio')


def send_message(event, namespace, room, message):
    print message
    socketio.emit(event,{'msg':message},namespace=namespace,room=room)

@celery.task
def long_task(n, session):
    room=session
    namespace='/long_task'

    send_message('status',namespace,room,'Begin')
    send_message('msg',namespace,room,'Begin task {}'.format(long_task.request.id))
    send_message('msg',namespace,room,'This task will take {} seconds.'.format(n))

    for i in range(n):
        send_message('msg',namespace,room,str(i))
        time.sleep(1)

    send_message('msg',namespace,room,'End Task {}'.format(long_task.request.id))
    send_message('status',namespace,room,'End')

