import time, threading
import requests
import plotext
from flask import Flask, request

plotext.plot_size(20)
plotext.bar(['VMs'], [1], width = .1)
plotext.ylim(0, 100)
plotext.yticks([i * 10 for i in range(11)])
plotext.bar(['VMs'], [0])
plotext.interactive(True)

app = Flask(__name__)
# A map from IPs that contacted us => last time we heard from them
app.ips = {}

@app.route("/")
def checkin():
    app.ips[request.remote_addr] = time.time()
    return "okay"

@app.route("/refresh")
def refresh():
    active = len([ip for ip, last in app.ips.items() if last > time.time() - 10])
    if active == 1:
        plotext.bar(['1 VM'], [1])
    else:
        plotext.bar([str(active) + ' VMs'], [active])
    return "okay"

def get_self():
    while 1:
        time.sleep(1)
        requests.get('http://127.0.0.1:5000/refresh')

t = threading.Thread(target=get_self)
t.start()
