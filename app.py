from flask import Flask, jsonify, render_template
import pandas as pd
import pickle
import random

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Simulated sensor data (replace with ESP32 later)
def get_sensor_data():
    return {
        "current": random.randint(200, 800),
        "voltage": random.randint(1200, 1700),
        "temp": random.randint(300, 600)
    }

# Serve dashboard
@app.route("/")
def home():
    return render_template("index.html")

# API endpoint
@app.route("/data")
def get_data():
    d = get_sensor_data()

    input_df = pd.DataFrame([d])
    pred = int(model.predict(input_df)[0])

    return jsonify({
        "current": d["current"],
        "voltage": d["voltage"],
        "temp": d["temp"],
        "prediction": pred
    })

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)