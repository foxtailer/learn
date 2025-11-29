import requests

# Replace with your bot's token
BOT_TOKEN = ""

# The URL for deleting the webhook
delete_webhook_url = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook"

# Make the POST request to delete the webhook
response = requests.post(delete_webhook_url)

# Check the response from Telegram
if response.status_code == 200:
    print("Webhook deleted successfully!")
    print(response.json())
else:
    print(f"Failed to delete webhook. Status code: {response.status_code}")
    print(response.text)