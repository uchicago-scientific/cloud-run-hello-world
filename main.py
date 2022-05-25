import os, datetime, json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
  return "Hello Photo Timeline!", 200

if __name__ == '__main__':
  app.run(debug=True)
