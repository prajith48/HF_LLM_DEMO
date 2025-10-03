import requests, os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

OUTPUT_DIR = "outputs"

def summarize(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def run_summarizer():
    text = input("Enter text to summarize: ")
    result = summarize(text)
    summary = result[0]['summary_text']

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_path = os.path.join(OUTPUT_DIR, "summary.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(summary)

    print(f"✅ Summary saved at: {file_path}")
