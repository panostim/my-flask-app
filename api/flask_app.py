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
                <title>Responsive Flask App</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        flex-direction: column;
                        justify-content: top;
                        align-items: center;
                        text-align: center;
                        min-height: 100vh;
                        background: linear-gradient(to bottom, #ece9e6, #ffffff);
                    }}
                    h1 {{
                        color: #333;
                        font-size: 2rem;
                        margin-bottom: 20px;
                    }}
                    p {{
                        color: #555;
                        font-size: 1.2rem;
                        margin: 10px 0;
                    }}
                    @media (max-width: 600px) {{
                        h1 {{
                            font-size: 1.5rem;
                        }}
                        p {{
                            font-size: 1rem;
                        }}
                    }}
                </style>
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
            <body>
                <h1>Responsive Flask App with Dynamic Time</h1>
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
