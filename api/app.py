from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
import sys
import pandas as pd

# Modify path for Vercel
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from ml.train_model import extract_features

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load the trained model
try:
    model_path = os.path.join(project_root, 'phishing_model.pkl')
    model = joblib.load(model_path)
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None

@app.route('/')
def index():
    return jsonify({
        "message": "ML Phishing Detection API",
        "status": "healthy",
        "version": "1.0.0"
    }), 200

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({
            "error": "Model not loaded",
            "status": "error"
        }), 500

    try:
        data = request.get_json()
        url = data.get('url', '')
        
        if not url:
            return jsonify({
                "error": "No URL provided",
                "status": "failed"
            }), 400
        
        # Extract features
        feature_df = pd.DataFrame([extract_features(url)])
        
        # Predict
        prediction = model.predict(feature_df)[0]
        probability = model.predict_proba(feature_df)[0][1]
        
        return jsonify({
            "url": url,
            "is_phishing": bool(prediction),
            "phishing_probability": float(probability),
            "status": "success"
        }), 200
    
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy" if model is not None else "model_error",
        "message": "API is running smoothly" if model is not None else "Model failed to load"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
