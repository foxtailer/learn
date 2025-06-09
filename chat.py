#!/usr/bin/env python3
import sys
import os
import requests
import json

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY environment variable not set")
    sys.exit(1)

API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

def generate_text(prompt: str) -> str:
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code != 200:
        print(f"API request failed with status {response.status_code}: {response.text}")
        sys.exit(1)
    
    resp_json = response.json()
    try:
        # Extract the generated text
        text = resp_json["candidates"][0]["content"]["parts"][0]["text"]
        return text.strip()
    except (KeyError, IndexError) as e:
        print("Failed to parse API response:", e)
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} 'your prompt here'")
        sys.exit(1)
    
    prompt = " ".join(sys.argv[1:])
    generated = generate_text(prompt)
    print("\n=== Generated Text ===\n")
    print(generated)
    print("\n======================")

if __name__ == "__main__":
    main()

