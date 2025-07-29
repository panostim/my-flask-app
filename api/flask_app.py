from flask import Flask
from flask_cors import CORS
from datetime import datetime
import os
import requests

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

CITIES = ["New York", "London", "Athens", "New Delhi"]

# API key for OpenWeather. The value can be overridden by setting the
# OPENWEATHER_API_KEY environment variable.
API_KEY = os.getenv("OPENWEATHER_API_KEY", "4d4fb0b31ee1cf8263a476b0b6c82341")

def get_weather(city):
    """Fetch weather information for a city using OpenWeather API."""
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        resp = requests.get(url, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        temp = data.get("main", {}).get("temp")
        wind = data.get("wind", {}).get("speed")
        if temp is not None and wind is not None:
            return f"{city}: {temp}\N{DEGREE SIGN}C, Wind {wind} m/s"
    except Exception:
        pass
    return f"{city}: N/A"

@app.route("/", methods=["GET"])
def home():
    now = datetime.utcnow()
    initial_time = now.isoformat() + "Z"
    weather_info = "".join(f"<p>{get_weather(city)}</p>" for city in CITIES)
    return f"""
        <html>
            <head>
                <title>Responsive Flask App</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 100px;
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
                <h1>Dynamic Time and Weather Information Web App</h1>
                <p><br>This is a responsive app that displays the current weather for several cities using data from the OpenWeather API and updates the time every second.</p>
                <p><br><strong>Current Time:</strong></p>
                <p><strong>Date and Time (UTC):</strong> <span id="current-time">{initial_time.split('T')[0]} {initial_time.split('T')[1][:-1]}</span></p>
                <p><strong>ISO Timestamp:</strong> <span id="timestamp">{initial_time}</span></p>
                <p><br><strong>Weather Information:</strong></p>
                {weather_info}
                <p><br>Tech Stack: Python Flask, Flask-CORS, Requests, React</p>
                <p><br>Powered by Panos</p>

            </body>
        </html>
    """

@app.route("/api/timestamp", methods=["GET"])
def get_timestamp():
    now = datetime.utcnow()
    return {"timestamp": now.isoformat() + "Z"}

# Expose the app for Vercel
app = app
