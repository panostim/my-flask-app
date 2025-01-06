from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/api/timestamp", methods=["GET"])
def get_timestamp():
    now = datetime.utcnow()
    return jsonify({"timestamp": now.isoformat() + "Z"})

# The Vercel serverless environment requires this handler
def handler(event, context):
    from flask import request
    return app.wsgi_app(event, context)
