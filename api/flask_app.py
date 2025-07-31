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
    weather_info = "".join(f'<div class="weather-card"><span class="weather-icon">🌤️</span><span class="weather-text">{get_weather(city)}</span></div>' for city in CITIES)
    return f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Modern Flask App</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
                <style>
                    * {{
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                    }}

                    :root {{
                        --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                        --card-bg: rgba(255, 255, 255, 0.1);
                        --card-border: rgba(255, 255, 255, 0.2);
                        --text-primary: #ffffff;
                        --text-secondary: rgba(255, 255, 255, 0.8);
                        --shadow-light: 0 8px 32px rgba(0, 0, 0, 0.1);
                        --shadow-heavy: 0 20px 60px rgba(0, 0, 0, 0.15);
                        --border-radius: 20px;
                        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                    }}

                    body {{
                        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                        line-height: 1.6;
                        color: var(--text-primary);
                        min-height: 100vh;
                        background: var(--primary-gradient);
                        position: relative;
                        overflow-x: hidden;
                    }}

                    .background-overlay {{
                        position: fixed;
                        top: 0;
                        left: 0;
                        width: 100%;
                        height: 100%;
                        background: var(--secondary-gradient);
                        opacity: 0.3;
                        animation: gradientShift 8s ease-in-out infinite;
                        z-index: -1;
                    }}

                    @keyframes gradientShift {{
                        0%, 100% {{ opacity: 0.3; }}
                        50% {{ opacity: 0.6; }}
                    }}



                    .container {{
                        max-width: 1200px;
                        margin: 0 auto;
                        padding: 2rem;
                        position: relative;
                        z-index: 1;
                    }}

                    .header {{
                        text-align: center;
                        margin-bottom: 3rem;
                        animation: fadeInUp 0.8s ease-out;
                    }}

                    .title {{
                        font-size: 3.5rem;
                        font-weight: 700;
                        margin-bottom: 1rem;
                        background: linear-gradient(45deg, #ffffff, #f0f0f0);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        background-clip: text;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        gap: 1rem;
                    }}

                    .title-icon {{
                        font-size: 3rem;
                        animation: pulse 2s ease-in-out infinite;
                    }}

                    .subtitle {{
                        font-size: 1.2rem;
                        color: var(--text-secondary);
                        font-weight: 400;
                        margin-bottom: 2rem;
                    }}

                    @keyframes pulse {{
                        0%, 100% {{ transform: scale(1); }}
                        50% {{ transform: scale(1.1); }}
                    }}

                    .content-grid {{
                        display: grid;
                        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                        gap: 2rem;
                        margin-bottom: 3rem;
                    }}

                    .card {{
                        background: var(--card-bg);
                        backdrop-filter: blur(20px);
                        border: 1px solid var(--card-border);
                        border-radius: var(--border-radius);
                        padding: 2rem;
                        box-shadow: var(--shadow-light);
                        transition: var(--transition);
                        animation: fadeInUp 0.8s ease-out;
                    }}

                    .card:hover {{
                        transform: translateY(-5px);
                        box-shadow: var(--shadow-heavy);
                        border-color: rgba(255, 255, 255, 0.3);
                    }}

                    .card-header {{
                        display: flex;
                        align-items: center;
                        gap: 1rem;
                        margin-bottom: 1.5rem;
                    }}

                    .card-icon {{
                        font-size: 1.5rem;
                        animation: bounce 2s ease-in-out infinite;
                    }}

                    .card-title {{
                        font-size: 1.3rem;
                        font-weight: 600;
                        color: var(--text-primary);
                    }}

                    @keyframes bounce {{
                        0%, 100% {{ transform: translateY(0); }}
                        50% {{ transform: translateY(-5px); }}
                    }}

                    .time-display {{
                        font-size: 2.5rem;
                        font-weight: 600;
                        color: var(--text-primary);
                        font-family: 'JetBrains Mono', 'Fira Code', monospace;
                        background: linear-gradient(45deg, #ffffff, #e0e0e0);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        background-clip: text;
                        text-align: center;
                    }}

                    .timestamp-display {{
                        font-size: 1.4rem;
                        font-weight: 600;
                        color: var(--text-primary);
                        font-family: 'JetBrains Mono', 'Fira Code', monospace;
                        background: linear-gradient(45deg, #ffffff, #e0e0e0);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        background-clip: text;
                        word-break: break-all;
                    }}

                    .weather-grid {{
                        display: grid;
                        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                        gap: 1rem;
                    }}

                    .weather-card {{
                        background: rgba(255, 255, 255, 0.05);
                        border: 1px solid rgba(255, 255, 255, 0.1);
                        border-radius: 15px;
                        padding: 1rem;
                        display: flex;
                        align-items: center;
                        gap: 0.5rem;
                        transition: var(--transition);
                    }}

                    .weather-card:hover {{
                        background: rgba(255, 255, 255, 0.1);
                        transform: translateY(-2px);
                    }}

                    .weather-icon {{
                        font-size: 1.2rem;
                    }}

                    .weather-text {{
                        color: var(--text-primary);
                        font-weight: 500;
                    }}

                    .footer {{
                        text-align: center;
                        margin-top: 3rem;
                        animation: fadeInUp 0.8s ease-out 0.4s both;
                    }}

                    .footer p {{
                        color: var(--text-secondary);
                        margin-bottom: 1rem;
                        font-size: 1.1rem;
                    }}

                    .tech-stack {{
                        display: flex;
                        justify-content: center;
                        gap: 1rem;
                        flex-wrap: wrap;
                    }}

                    .tech-badge {{
                        background: rgba(255, 255, 255, 0.1);
                        border: 1px solid rgba(255, 255, 255, 0.2);
                        border-radius: 25px;
                        padding: 0.5rem 1rem;
                        font-size: 0.9rem;
                        font-weight: 500;
                        color: var(--text-primary);
                        transition: var(--transition);
                    }}

                    .tech-badge:hover {{
                        background: rgba(255, 255, 255, 0.2);
                        transform: translateY(-2px);
                    }}

                    @keyframes fadeInUp {{
                        from {{
                            opacity: 0;
                            transform: translateY(30px);
                        }}
                        to {{
                            opacity: 1;
                            transform: translateY(0);
                        }}
                    }}

                    @media (max-width: 768px) {{
                        .container {{
                            padding: 1rem;
                        }}
                        
                        .title {{
                            font-size: 2.5rem;
                            flex-direction: column;
                            gap: 0.5rem;
                        }}
                        
                        .title-icon {{
                            font-size: 2rem;
                        }}
                        
                        .subtitle {{
                            font-size: 1rem;
                        }}
                        
                        .content-grid {{
                            grid-template-columns: 1fr;
                            gap: 1.5rem;
                        }}
                        
                        .card {{
                            padding: 1.5rem;
                        }}
                        
                        .time-display {{
                            font-size: 2rem;
                        }}
                        
                        .timestamp-display {{
                            font-size: 1.2rem;
                        }}
                        
                        .weather-grid {{
                            grid-template-columns: 1fr;
                        }}
                        
                        .tech-stack {{
                            gap: 0.5rem;
                        }}
                        
                        .tech-badge {{
                            padding: 0.4rem 0.8rem;
                            font-size: 0.8rem;
                        }}
                    }}

                    @media (max-width: 480px) {{
                        .title {{
                            font-size: 2rem;
                        }}
                        
                        .time-display {{
                            font-size: 1.8rem;
                        }}
                        
                        .timestamp-display {{
                            font-size: 1.1rem;
                        }}
                    }}

                    html {{
                        scroll-behavior: smooth;
                    }}

                    *:focus {{
                        outline: 2px solid rgba(255, 255, 255, 0.5);
                        outline-offset: 2px;
                    }}

                    ::selection {{
                        background: rgba(255, 255, 255, 0.3);
                        color: var(--text-primary);
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
                <div class="background-overlay"></div>
                
                <div class="container">
                    <header class="header">
                        <h1 class="title">
                            <span class="title-icon">⏰</span>
                            Dynamic Time & Weather
                        </h1>
                        <p class="subtitle">Real-time weather information and synchronized time display</p>
                    </header>

                    <div class="content-grid">
                        <div class="card">
                            <div class="card-header">
                                <span class="card-icon">🕐</span>
                                <h2 class="card-title">Current Time (UTC)</h2>
                            </div>
                            <div class="time-display" id="current-time">{initial_time.split('T')[0]} {initial_time.split('T')[1][:-1]}</div>
                        </div>

                        <div class="card">
                            <div class="card-header">
                                <span class="card-icon">⚡</span>
                                <h2 class="card-title">ISO Timestamp</h2>
                            </div>
                            <div class="timestamp-display" id="timestamp">{initial_time}</div>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-header">
                            <span class="card-icon">🌤️</span>
                            <h2 class="card-title">Weather Information</h2>
                        </div>
                        <div class="weather-grid">
                            {weather_info}
                        </div>
                    </div>

                    <footer class="footer">
                        <p>Built with modern web technologies</p>
                        <div class="tech-stack">
                            <span class="tech-badge">Python Flask</span>
                            <span class="tech-badge">Flask-CORS</span>
                            <span class="tech-badge">OpenWeather API</span>
                            <span class="tech-badge">Modern CSS</span>
                        </div>
                        <p style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.7;">Powered by Panos</p>
                    </footer>
                </div>
            </body>
        </html>
    """

@app.route("/api/timestamp", methods=["GET"])
def get_timestamp():
    now = datetime.utcnow()
    return {"timestamp": now.isoformat() + "Z"}

# Expose the app for Vercel
app = app
