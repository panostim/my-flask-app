from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/", methods=["GET"])
def home():
    return "Flask app is running!"

@app.route("/api/timestamp", methods=["GET"])
def get_timestamp():
    now = datetime.utcnow()
    return jsonify({"timestamp": now.isoformat() + "Z"})

# Required for Vercel's serverless environment
# Rename this to app as it is automatically detected by Vercel
app = app
