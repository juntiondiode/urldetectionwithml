chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.url) {
        fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({url: changeInfo.url})
        })
        .then(response => response.json())
        .then(data => {
            if (data.is_phishing) {
                chrome.action.setBadgeText({text: '⚠️', tabId: tabId});
                chrome.action.setBadgeBackgroundColor({color: '#ff0000', tabId: tabId});
                
                // Show notification for high-risk sites
                if (data.probability > 0.8) {
                    chrome.notifications.create({
                        type: 'basic',
                        iconUrl: 'icons/icon48.png',
                        title: 'Phishing Alert!',
                        message: 'This website has been detected as a potential phishing site. Please be careful!'
                    });
                }
            } else {
                chrome.action.setBadgeText({text: '✓', tabId: tabId});
                chrome.action.setBadgeBackgroundColor({color: '#00ff00', tabId: tabId});
            }
        })
        .catch(error => {
            console.error('Error:', error);
            chrome.action.setBadgeText({text: '?', tabId: tabId});
            chrome.action.setBadgeBackgroundColor({color: '#ffff00', tabId: tabId});
        });
    }
});
