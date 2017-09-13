from flask import Flask, render_template, redirect, url_for, request, jsonify, session
from flask_socketio import SocketIO, join_room
from random import randint
import uuid
import tasks
import eventlet

eventlet.monkey_patch()

app=Flask(__name__)
app.secret_key="DataRoadReflect"

socketio = SocketIO(app, message_queue='amqp:///socketio')


@app.route("/", methods=['GET'])
def index():

    # create a unique session id

    if 'uid' not in session:
        session['uid']=str(uuid.uuid4())

    return render_template('index.html')


@app.route("/runTask", methods=['POST'])
def long_task():

    n=randint(0,100)
    sid=str(session['uid'])
    task=tasks.long_task.delay(n=n, session=sid)

    return  jsonify({'id':task.id})


@socketio.on('connect')
def socket_connect():
    pass

@socketio.on('join_room',namespace='/long_task')
def on_room():

    room=str(session['uid'])

    print 'join room {}'.format(room)

    join_room(room)


if __name__=="__main__":

    socketio.run(app,debug=True, host="0.0.0.0")


