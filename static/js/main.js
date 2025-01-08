document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const cityInput = document.querySelector("input[name='city']");
    
    form.addEventListener("submit", (event) => {
        if (cityInput.value.trim() === "") {
            event.preventDefault();
            alert("Please enter a city name!");
        }
    });

    const body = document.body;
    const weatherId = body.getAttribute("data-weather-id");

    if (weatherId) {
        const weatherIdNum = parseInt(weatherId, 10);
        let weatherClass = "clear-sky";

        if (weatherIdNum >= 200 && weatherIdNum < 300) {
            weatherClass = "thunder"; // Thunderstorm
        } else if (weatherIdNum >= 300 && weatherIdNum < 400) {
            weatherClass = "drizzle"; // Drizzle
        } else if (weatherIdNum >= 500 && weatherIdNum < 600) {
            weatherClass = "rain"; // Rain
        } else if (weatherIdNum >= 600 && weatherIdNum < 700) {
            weatherClass = "snow"; // Snow
        } else if (weatherIdNum >= 700 && weatherIdNum < 800) {
            weatherClass = "mist"; // Atmosphere (e.g., mist, fog)
        } else if (weatherIdNum === 800) {
            weatherClass = "clear-sky"; // Clear sky
        } else if (weatherIdNum > 800) {
            weatherClass = "cloudy"; // Cloudy
        }

        // Update body class
        body.className = weatherClass;
    } else {
        // Default class if no weather ID is provided
        body.className = "clear-sky";
    }
});
