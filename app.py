from flask import Flask
from redis import Redis, RedisError
import os
import socket
#import subprocess

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=1, socket_timeout=1)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello from Docker <b>{name}</b>!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}<br/>"\
           #"<b>Container IP:</b> {ip}"
    return html.format(name=os.getenv("NAME"), hostname=socket.gethostname(), visits=visits)
    #return html.format(name=os.getenv("NAME", "CondorLabs"), hostname=socket.gethostname(), visits=visits, ip=subprocess.check_output(['bash', '-c', "/sbin/ip route|awk 'NR==2{print $9}'"]).decode('utf-8').strip())
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
