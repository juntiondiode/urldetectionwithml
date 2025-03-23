from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import os
import sys
import pandas as pd

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from ml.train_model import extract_features

app = Flask(__name__)
CORS(app)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'phishing_model.pkl')
model = joblib.load(model_path)

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Predict if a URL is phishing"""
    try:
        # Get URL from request
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({'error': 'No URL provided'}), 400
        
        url = data['url']
        
        # Extract features
        features = extract_features(url)
        
        # Convert features to DataFrame
        feature_df = pd.DataFrame([features])
        
        # Get prediction and probability
        prediction = model.predict(feature_df)[0]
        probability = model.predict_proba(feature_df)[0][1]
        
        # Only include the features we're actually using
        relevant_features = {
            'url_length': features['url_length'],
            'domain_length': features['domain_length'],
            'num_dots': features['num_dots'],
            'has_hyphen': features['has_hyphen'],
            'has_at': features['has_at'],
            'num_subdomains': features['num_subdomains'],
            'is_https': features['is_https'],
            'dns_resolved': features['dns_resolved']
        }
        
        return jsonify({
            'prediction': int(prediction),
            'probability': float(probability),
            'features': relevant_features,
            'status': 'success'
        })
        
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
