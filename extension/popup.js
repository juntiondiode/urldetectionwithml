document.addEventListener('DOMContentLoaded', function() {
    const currentUrlElement = document.getElementById('currentUrl');
    const resultContainer = document.getElementById('resultContainer');
    const resultText = document.getElementById('resultText');
    const statusIcon = document.getElementById('statusIcon');
    const details = document.getElementById('details');
    const scanButton = document.getElementById('scanButton');
    const spinner = document.getElementById('spinner');

    // API endpoint
    const API_URL = 'http://localhost:5000/predict';

    // Get current tab URL
    function getCurrentTabUrl(callback) {
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            callback(tabs[0].url);
        });
    }

    // Update UI elements based on prediction
    function updateUI(prediction, probability, url) {
        spinner.style.display = 'none';
        scanButton.disabled = false;

        // Update current URL display
        currentUrlElement.textContent = url;

        // Remove previous status classes
        resultContainer.classList.remove('loading', 'safe', 'unsafe');

        if (prediction === 0) {
            // Legitimate URL
            resultContainer.classList.add('safe');
            statusIcon.src = 'safe.png';
            resultText.textContent = 'Safe Website';
            details.textContent = `This website appears to be legitimate with ${(probability * 100).toFixed(2)}% confidence.`;
        } else {
            // Phishing URL
            resultContainer.classList.add('unsafe');
            statusIcon.src = 'unsafe.png';
            resultText.textContent = 'Warning: Potential Phishing';
            details.textContent = `This website might be a phishing attempt with ${(probability * 100).toFixed(2)}% probability. Be careful with sharing any sensitive information.`;
        }
    }

    // Handle API errors
    function handleError(error) {
        spinner.style.display = 'none';
        scanButton.disabled = false;
        resultContainer.classList.remove('loading', 'safe', 'unsafe');
        resultContainer.classList.add('unsafe');
        statusIcon.src = 'error.png';
        resultText.textContent = 'Error';
        details.textContent = 'Could not analyze the URL. Please make sure the API server is running and try again.';
        console.error('Error:', error);
    }

    // Analyze URL using the API
    function analyzeUrl(url) {
        // Show loading state
        spinner.style.display = 'block';
        scanButton.disabled = true;
        resultContainer.classList.add('loading');
        statusIcon.src = 'loading.png';
        resultText.textContent = 'Analyzing URL...';
        details.textContent = 'Please wait while we analyze the website...';

        // Make API request
        fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: url })
        })
        .then(response => response.json())
        .then(data => {
            updateUI(data.prediction, data.probability, url);
        })
        .catch(error => {
            handleError(error);
        });
    }

    // Initialize popup
    function initPopup() {
        getCurrentTabUrl(function(url) {
            currentUrlElement.textContent = url;
            // Don't auto-analyze, wait for user to click scan button
        });
    }

    // Add click event listener to scan button
    scanButton.addEventListener('click', function() {
        getCurrentTabUrl(function(url) {
            analyzeUrl(url);
        });
    });

    // Initialize popup when opened
    initPopup();
});
