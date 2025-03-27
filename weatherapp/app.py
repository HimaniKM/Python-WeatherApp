from flask import Flask, request, jsonify,render_template
import requests

app = Flask(__name__)

# Replace with your actual API key from OpenWeatherMap
API_KEY = "377494fb25b4200bf9c068a2798af16c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Get temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code != 200:
        return jsonify({"error": "City not found"}), 404
    
    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"].capitalize()
    }
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
