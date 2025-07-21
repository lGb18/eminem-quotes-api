

from flask import Flask, jsonify
import json,random
app = Flask(__name__)

with open('quotes.json') as file:
    quotes = json.load(file)
@app.route('/')
def index():
    return jsonify({"quotes": random.choice(quotes)})

