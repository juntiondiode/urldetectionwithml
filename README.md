# ML-Based Phishing Detection Chrome Extension

A powerful Chrome extension that uses machine learning to detect potential phishing websites in real-time. The extension analyzes URLs based on various features and provides instant feedback about the safety of websites you visit.

## Features

- **Real-time URL Analysis**: Instantly analyzes URLs as you browse
- **Machine Learning Model**: Uses a Random Forest classifier trained on key URL features
- **Visual Feedback**: 
  - Green checkmark (✓) for safe websites
  - Red warning (⚠️) for potential phishing sites
  - Detailed analysis view in the popup
- **High Accuracy**: Achieves over 99% accuracy in phishing detection
- **Lightweight**: Uses simplified features for quick analysis
- **User-friendly Interface**: Clean, modern UI with detailed insights

## Project Structure
```
urldetectionwithml/
├── api/                    # Flask API server
│   └── app.py             # Main API implementation
├── data/                  # Dataset and data processing
│   └── dataset.csv       # Training dataset
├── extension/            # Chrome extension files
│   ├── manifest.json    # Extension configuration
│   ├── popup.html      # Extension popup UI
│   ├── popup.js       # Popup functionality
│   └── background.js  # Background service worker
└── ml/                # Machine learning components
    └── train_model.py # Model training script
```

## Key Features Used for Detection

- URL length
- Domain length
- Number of dots in domain
- Presence of hyphens
- Presence of @ symbol
- Number of subdomains
- HTTPS usage
- DNS resolution status

## Setup Instructions

1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

2. **Start the API Server**:
```bash
python api/app.py
```
The server will run on `http://localhost:5000`

3. **Load the Chrome Extension**:
- Open Chrome browser
- Navigate to `chrome://extensions/`
- Enable "Developer mode" (top right toggle)
- Click "Load unpacked"
- Select the `extension` folder from this project

## Usage

1. After installation, you'll see the extension icon in your Chrome toolbar
2. The icon will automatically update as you browse:
   - ✓ (Green): Safe website
   - ⚠️ (Red): Potential phishing site
3. Click the icon to see detailed analysis of the current URL
4. For high-risk sites (>80% probability), you'll receive a notification

## Technical Details

- **Backend**: Flask-based RESTful API
- **Model**: Random Forest Classifier
- **Training Data**: Curated dataset of legitimate and phishing URLs
- **Feature Extraction**: Real-time URL analysis
- **Browser Integration**: Chrome Extension API
- **Response Time**: <1 second for analysis

## Requirements

- Python 3.7+
- Chrome Browser
- Required Python packages (see requirements.txt)
- Active internet connection for DNS checks

## Contributing

Feel free to contribute to this project by:
1. Reporting issues
2. Suggesting new features
3. Submitting pull requests

## License

This project is licensed under the MIT License - see the LICENSE file for details.
