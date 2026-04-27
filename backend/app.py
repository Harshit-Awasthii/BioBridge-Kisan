from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "f4d57d6586f9f419b818d2d819a6f483"
CITY = "Delhi"

@app.route("/weather")
def get_weather():
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        print("Weather API response:", data)

        if response.status_code != 200:
            return jsonify({
                "error": data.get("message", "Failed to fetch weather")
            }), response.status_code

        return jsonify({
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        })

    except Exception as e:
        print("Weather error:", e)
        return jsonify({"error": "Failed to fetch weather"}), 500

# load trained model
model = pickle.load(open("ai-model/model.pkl", "rb"))
# model = pickle.load(open("crop_model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    N = data["N"]
    P = data["P"]
    K = data["K"]
    temperature = data["temperature"]
    humidity = data["humidity"]
    ph = data["ph"]
    rainfall = data["rainfall"]

    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    prediction = model.predict(features)

    return jsonify({
        "recommended_crop": prediction[0]
    })


if __name__ == "__main__":
    app.run(debug=True)