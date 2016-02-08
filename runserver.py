from flask import Flask, request, redirect, jsonify, url_for
import requests
app = Flask(__name__)

@app.route('/')
def base_path():
    return 'working'

@app.route('/<path:path>')
def redirect(path):
    url = 'http://localhost:5000/' + path
    print(request.method)
    print(url)
    r = requests.request(request.method, url)
    return r.content

    # r = {}
    # if request.method == 'POST':
    #     r = requests.post("http://localhost:5000", data = {"key":"value"})
    # else if request.method == 'GET':
    #     r = requests.get("http://localhost:5000"
    # return r

if __name__ == '__main__':
    app.run(debug = True, port = 5001)
