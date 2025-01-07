from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "d49e7db39431b066df9cb515578885d8"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            # Call OpenWeather API
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
