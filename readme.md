A small, responsive and dynamic app displaying current time, date and timestamp.

The app is using Python Flask to create an API for the backend (e.g. current timestamp).

The content is dynamic using React JS.

The app fetches weather information using the OpenWeather API and displays the
conditions for New York, London, Athens and New Delhi above the timestamp.

## Accessible online

The app is deployed on Vercel and is accessible in:
https://date-time-ten.vercel.app/

## Running locally

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Flask development server:
   ```bash
   FLASK_APP=api/flask_app.py flask run
   ```
4. Open `http://localhost:5000` in your browser to view the app.

The OpenWeather API key is already embedded in `api/flask_app.py`. If you wish to
use your own key, edit `API_KEY` at the top of that file.