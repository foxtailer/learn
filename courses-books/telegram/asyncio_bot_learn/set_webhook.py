import requests

# Replace with your bot's token
BOT_TOKEN = ""

# Replace with your webhook URL
WEBHOOK_URL = ""

# The URL for setting the webhook
set_webhook_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"

# Data to send in the POST request
data = {
    "url": WEBHOOK_URL
}

# Make the POST request to set the webhook
response = requests.post(set_webhook_url, data=data)

# Check the response from Telegram
if response.status_code == 200:
    print("Webhook set successfully!")
    print(response.json())
else:
    print(f"Failed to set webhook. Status code: {response.status_code}")
    print(response.text)