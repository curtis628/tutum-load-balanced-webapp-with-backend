from flask import Flask
import urllib2
import os
import socket

app = Flask(__name__)

@app.route("/")
def index():
    greetingURL = "http://greeting-rest-haproxy"
    greetingResponse = urllib2.urlopen(greetingURL)
    greeting = greetingResponse.read()
    html = "<h3>{appname}</h3>" \
           "<b>WebApp Host:</b> {hostname}<br/>" \
           "<b>Greeting API URL:</b> {greetingURL}<br/>" \
           "<b>Greeting Response:</b> {greeting}"
    return html.format(appname=os.getenv('APPNAME', "WebApp"),
                       hostname=socket.gethostname(),
                       greetingURL=greetingURL,
                       greeting=greeting)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
