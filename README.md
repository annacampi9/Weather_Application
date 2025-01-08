# Weather Application 🌤️

A simple weather app built with Python, Flask, and the OpenWeatherMap API. This app displays the current weather for a city and dynamically updates the background based on weather conditions.

---

## Features

- Search for weather conditions by city name 🌎
- Dynamic background images based on weather conditions (e.g., Clear Sky, Clouds, Rain, etc.) 🎨
- Error handling for invalid city names or API issues ⚠️
- Environment variable support for securing the OpenWeather API key 🔐

---

## Prerequisites

1. **Python** (version 3.7 or higher)
2. **pip** (Python package installer)
3. **An OpenWeatherMap API Key** (Sign up at [OpenWeatherMap](https://openweathermap.org/api) to get your free API key)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/weather_application.git
   cd weather_application
    ```
2. Create a .env file in the project directory and add your API key:

   ```bash
   OPENWEATHER_API_KEY=your_api_key_here
   ```

## Dynamic Backgrounds

The app dynamically updates the background based on the `weather_id` from the OpenWeatherMap API. The mappings are as follows:

| Weather Group | Description      | Background Image |
|---------------|------------------|------------------|
| 2xx           | Thunderstorm     | `thunder.jpg`    |
| 3xx           | Drizzle          | `mist.jpg`       |
| 5xx           | Rain             | `rain.jpg`       |
| 6xx           | Snow             | `snow.jpg`       |
| 8xx (800)     | Clear Sky        | `clear_sky.jpg`  |
| 8xx (801-804) | Clouds           | `cloudy.jpg`     |

---

## Future Improvements

Here are a few potential improvements and features that could be added to the app in the future:

- **5-Day Forecast**
  
- **User Location**
  
- **Weather Alerts**
  
- **Performance Optimization**

- **Mobile-Friendly**

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
