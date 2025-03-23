import requests
import json

def test_url(url):
    """Test a URL against the phishing detection API"""
    api_url = 'http://localhost:5000/predict'
    response = requests.post(api_url, json={'url': url})
    
    print(f"Testing URL: {url}")
    print("Result:")
    print(json.dumps(response.json(), indent=2))
    print()

def main():
    """Test the ML Phishing Detection API"""
    print("Testing ML Phishing Detection API...\n")
    
    # Test legitimate URLs
    print("=== Testing Legitimate URLs ===\n")
    legitimate_urls = [
        'https://www.google.com',
        'https://www.microsoft.com',
        'https://www.github.com'
    ]
    
    for url in legitimate_urls:
        test_url(url)
    
    # Test suspicious URLs
    print("=== Testing Suspicious URLs ===\n")
    suspicious_urls = [
        'http://secure-paypal.com.verify.account.com',
        'http://googgle-security.com',
        'http://paypal-secure.phishing.com',
        'http://banking.secure.login.com'
    ]
    
    for url in suspicious_urls:
        test_url(url)

if __name__ == '__main__':
    main()
