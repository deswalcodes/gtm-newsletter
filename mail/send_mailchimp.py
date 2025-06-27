import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MAILCHIMP_API_KEY")
AUDIENCE_ID = os.getenv("MAILCHIMP_AUDIENCE_ID")
FROM_EMAIL = os.getenv("MAILCHIMP_FROM_EMAIL")  # <-- added

# datacenter is the prefix in the API key after the dash
DATACENTER = API_KEY.split('-')[-1]

def send_newsletter(subject, html_content):
    url = f"https://{DATACENTER}.api.mailchimp.com/3.0/campaigns"
    headers = {
        "Authorization": f"apikey {API_KEY}",
        "Content-Type": "application/json"
    }

    # 1️⃣ Create a campaign
    campaign_payload = {
        "type": "regular",
        "recipients": {
            "list_id": AUDIENCE_ID
        },
        "settings": {
            "subject_line": subject,
            "title": subject,
            "from_name": "Priyanshu",      # You can change this to your name
            "reply_to": FROM_EMAIL         # <-- use the verified sender
        }
    }

    campaign_response = requests.post(url, json=campaign_payload, headers=headers)
    if campaign_response.status_code != 200:
        print("❌ Failed to create campaign:", campaign_response.json())
        return
    
    campaign_id = campaign_response.json()["id"]

    # 2️⃣ Set campaign content
    content_url = f"https://{DATACENTER}.api.mailchimp.com/3.0/campaigns/{campaign_id}/content"
    content_payload = {
        "html": html_content
    }
    content_response = requests.put(content_url, json=content_payload, headers=headers)
    if content_response.status_code != 200:
        print("❌ Failed to set campaign content:", content_response.json())
        return
    
    # 3️⃣ Send campaign
    send_url = f"https://{DATACENTER}.api.mailchimp.com/3.0/campaigns/{campaign_id}/actions/send"
    send_response = requests.post(send_url, headers=headers)
    if send_response.status_code == 204:
        print("✅ Newsletter sent successfully via Mailchimp!")
    else:
        print("❌ Failed to send campaign:", send_response.json())
