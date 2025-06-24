from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS  # We will also add CORS support here for convenience

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load scaler and model
scaler = joblib.load('scaler.pkl')
model = joblib.load('kmeans_model.pkl')

@app.route('/')
def home():
    return "Avocado Ripeness Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    required_features = ['firmness', 'hue', 'saturation', 'brightness',
                         'sound_db', 'weight_g', 'size_cm3', 'color_category_encoded']

    # Check if all required features are present
    for feature in required_features:
        if feature not in data:
            return jsonify({'error': f'Missing feature: {feature}'}), 400

    # Validate that all features are numeric
    try:
        features = [float(data[feature]) for feature in required_features]
    except (ValueError, TypeError):
        return jsonify({'error': 'All features must be numeric'}), 400

    # Log received data and features (optional)
    print("Received data:", data)
    print("Features after conversion:", features)

    # Prepare features for prediction
    input_array = np.array(features).reshape(1, -1)
    scaled_input = scaler.transform(input_array)
    cluster = model.predict(scaled_input)

    # Log prediction (optional)
    print(f"Predicted cluster: {cluster[0]}")

    return jsonify({'cluster': int(cluster[0])})

if __name__ == '__main__':
    app.run(debug=True)
