import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import re
import tld
from urllib.parse import urlparse
import socket
from datetime import datetime

def is_ip_address(domain):
    """Check if the domain is an IP address"""
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return bool(re.match(pattern, domain))

def check_for_brand_names(url):
    """Check for common brand names in URL"""
    brands = [
        'paypal', 'apple', 'amazon', 'microsoft', 'google', 'facebook', 'ebay', 
        'netflix', 'instagram', 'linkedin', 'twitter', 'whatsapp', 'gmail',
        'bank', 'hdfc', 'sbi', 'icici', 'axis', 'kotak', 'pnb', 'rbi'
    ]
    return 1 if any(brand in url for brand in brands) else 0

def extract_features(url):
    """Extract basic features from URL for phishing detection"""
    features = {}
    
    try:
        # Parse URL
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        
        # Basic URL features
        features['url_length'] = len(url)
        features['domain_length'] = len(domain)
        features['num_dots'] = domain.count('.')
        features['has_hyphen'] = 1 if '-' in domain else 0
        features['has_at'] = 1 if '@' in url else 0
        features['num_subdomains'] = len(domain.split('.')) - 1
        features['is_https'] = 1 if parsed.scheme == 'https' else 0
        
        # Try DNS resolution
        try:
            socket.gethostbyname(domain)
            features['dns_resolved'] = 1
        except:
            features['dns_resolved'] = 0
            
    except Exception as e:
        print(f"Error extracting features: {str(e)}")
        features = {
            'url_length': 0,
            'domain_length': 0,
            'num_dots': 0,
            'has_hyphen': 0,
            'has_at': 0,
            'num_subdomains': 0,
            'is_https': 0,
            'dns_resolved': 0
        }
    
    return features

def prepare_features(df):
    """Convert DataFrame of URLs into feature matrix"""
    features_list = []
    for url in df['url']:
        features = extract_features(url)
        features_list.append(features)
    
    return pd.DataFrame(features_list)

def train_model(X, y):
    """Train Random Forest model with basic parameters"""
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )
    model.fit(X, y)
    return model

def main():
    """Train the phishing detection model"""
    # Load dataset
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(script_dir, '..', 'data', 'dataset.csv')
    df = pd.read_csv(dataset_path)
    
    # Extract features
    print("Extracting features...")
    X = prepare_features(df)
    y = df['label']
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y  # Ensure balanced split
    )
    
    # Train model
    print("\nTraining model...")
    model = train_model(X_train, y_train)
    
    # Evaluate model
    accuracy = model.score(X_test, y_test)
    print(f"Model Accuracy: {accuracy:.2%}")
    
    # Print detailed classification report
    from sklearn.metrics import classification_report, confusion_matrix
    y_pred = model.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Print feature importance
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    print("\nTop 10 Most Important Features:")
    print(feature_importance.head(10))
    
    # Save model
    model_path = os.path.join(script_dir, '..', 'api', 'phishing_model.pkl')
    joblib.dump(model, model_path)
    print(f"\nModel saved to: {model_path}")

if __name__ == "__main__":
    main()
