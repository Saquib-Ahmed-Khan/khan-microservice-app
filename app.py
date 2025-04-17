from flask import Flask
import socket
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Khan Microservice!"

@app.route('/host')
def host():
    return f"Hostname: {socket.gethostname()}"

@app.route('/ip')
def ip():
    ip = requests.get('https://api.ipify.org').text
    return f"External IP: {ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
