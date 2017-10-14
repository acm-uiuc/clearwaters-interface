from flask import Flask, jsonify, request, abort, render_template
import logging
import os
import socket

app = Flask(__name__)

TCP_IP = 'clearwaters-000'
TCP_PORT = 8888
PORT= 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

@app.route('/', methods=['GET'])
def hello():
    return jsonify('Welcome to the Cluster API')

@app.route('/run_job', methods=['GET'])
def run_job():
    s.connect((TCP_IP, TCP_PORT))
    s.send({'CMD': 'TEST'})
    data = s.recv(4096)
    s.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
