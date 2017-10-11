from flask import Flask, jsonify, request, abort, render_template
import logging
import os

app = Flask(__name__)

PORT= 5000

@app.route('/', methods=['GET'])
def hello():
    return jsonify('Welcome to the Cluster API')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
