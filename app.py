from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Travel Itinerary AI!"

if __name__ == '__main__':
    app.run(debug=True)