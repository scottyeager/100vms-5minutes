import time, threading
import requests
import plotext
from flask import Flask, request

plotext.plot_size(20)
plotext.bar(['VMs'], [1], width = .1)
plotext.ylim(0, 100)
plotext.yticks([i * 10 for i in range(11)])
plotext.bar(['nodes'], [0])
plotext.interactive(True)

app = Flask(__name__)
app.i = -1

@app.route("/")
def increment():
    app.i+=1
    plotext.bar([str(app.i) + ' VMs'], [app.i])
    return "Incremented!"

@app.route("/request")
def requested():
    return str(request.remote_addr)

def get_self():
    while 1:
        time.sleep(1)
        requests.get('http://127.0.0.1:5000')

t = threading.Thread(target=get_self)
t.start()

def count_up():
    i = 1
    while i <= 100:
        time.sleep(.1)
        plotext.bar([str(i) + ' nodes'], [i])
        #plotext.text(str(i), x=1, y=i + 2)
        i+=1
