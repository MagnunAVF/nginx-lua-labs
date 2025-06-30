#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def hello():
    return Response("Hello", mimetype='text/plain')

@app.errorhandler(404)
def not_found(e):
    return Response("Not Found", mimetype='text/plain'), 404

def run_server():
    port = 1666

    print(f"Server started at port {port}")
    print(f"Visit http://localhost:{port}/ to test the API")

    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    run_server()
