import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    weather_id = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                weather_data = response.json()
                weather_id = weather_data.get('weather', [{}])[0].get('id')
            else:
                error_message = "City not found. Please check the spelling and try again."

    return render_template(
        "index.html",
        weather=weather_data,
        weather_id=weather_id,
        error_message=error_message
    )

if __name__ == "__main__":
    app.run(debug=True)
