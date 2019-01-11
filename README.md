# Flask Celery and SocketIO example

 
## Dependencies:
  1. sudo apt-get install rabbitmq-server
  2. sudo apt-get install python-pip python-dev build-essential

## Python Packages:
  1. sudo pip install flask
  2. sudo pip install celery
  3. sudo pip install flask-socketio
  4. sudo pip install gevent
  
## RabbitMQ config:
  1. sudo rabbitmqctl add_vhost socketio
  2. sudo rabbitmqctl set_permissions -p socketio guest ".*" ".*" ".*"

## To Run:
  1. navigate to the demo folder
  2. Start the web server with the following command:
     - python www.py
  3. Start the celery worker with the following command:
     - celery -A tasks worker --loglevel=info --concurrency=2
  4. Navigate to \<HOST\>:5000 in your web browser.
  
  
Any questions email chad@caoanalytics.com
