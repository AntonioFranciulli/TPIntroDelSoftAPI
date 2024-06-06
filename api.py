from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

if __name__ == '__main__': 
   app.run("127.0.0.1",port = "5050", debug = True)