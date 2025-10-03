
import os
import requests
from dotenv import load_dotenv

# --- Configuration ---
# Make sure your .env file has: HF_TOKEN=hf_xxx...
load_dotenv()
API_TOKEN = os.getenv("HF_TOKEN")
if not API_TOKEN:
    raise ValueError("HF_TOKEN not found in .env file. Please check your .env file.")

# This is a simple text classification model, not a TTS model. It's good for testing.
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}
# --- End Configuration ---

def run_test():
    """
    Makes a single, simple request to the Hugging Face API and prints the result.
    """
    print("--- Starting Connection Test ---")
    print(f"Attempting to connect to: {API_URL}")
    
    try:
        payload = {"inputs": "This is a test of the Hugging Face API."}
        response = requests.post(API_URL, headers=HEADERS, json=payload)

        print(f"Response Status Code: {response.status_code}")
        
        # This is the most important part. We want to see the raw text of the response.
        print(f"Response Body (Text): {response.text}")

        if response.status_code == 200:
            print("\n✅ SUCCESS: The connection worked and the API returned a valid response.")
            print("The problem is likely somewhere in the logic of the main application scripts.")
        else:
            print("\n❌ FAILURE: The API returned an error.")
            print("This confirms a network or security software issue on your computer is blocking the request.")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ CRITICAL FAILURE: Could not connect to the server at all.")
        print(f"Error: {e}")
        print("This strongly indicates a firewall, antivirus, or proxy is blocking the connection.")

    print("--- Test Complete ---")

if __name__ == "__main__":
    run_test()
