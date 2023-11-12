# hello.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/login")
def login():
    msg= 'Welcome to JSPR-Techblog'
    data = request.json
    return jsonify(data)
