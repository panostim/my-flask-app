from flask import Flask
from flask_cors import CORS
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/", methods=["GET"])
def home():
    now = datetime.utcnow()
    initial_time = now.isoformat() + "Z"
    return f"""
        <html>
            <head>
                <title>Flask App with Dynamic Time</title>
                <script>
                    function updateTime() {{
                        const currentTimeElement = document.getElementById('current-time');
                        const timestampElement = document.getElementById('timestamp');
                        const now = new Date();
                        
                        // Format Date and Time
                        const dateTimeString = now.toISOString().replace('T', ' ').split('.')[0];

                        // Update the elements dynamically
                        currentTimeElement.innerText = dateTimeString;
                        timestampElement.innerText = now.toISOString();
                    }}

                    // Update every second
                    setInterval(updateTime, 1000);
                </script>
            </head>
            <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
                <h1>Flask App with Dynamic Time</h1>
                <p><strong>Date and Time (UTC):</strong> <span id="current-time">{initial_time.split('T')[0]} {initial_time.split('T')[1][:-1]}</span></p>
                <p><strong>ISO Timestamp:</strong> <span id="timestamp">{initial_time}</span></p>
            </body>
        </html>
    """

@app.route("/api/timestamp", methods=["GET"])
def get_timestamp():
    now = datetime.utcnow()
    return {"timestamp": now.isoformat() + "Z"}

# Expose the app for Vercel
app = app
