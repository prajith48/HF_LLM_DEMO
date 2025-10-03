import requests, os
from dotenv import load_dotenv
load_dotenv()
API_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/togethercomputer/RedPajama-INCITE-7B-Instruct"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

OUTPUT_DIR = "outputs"

def query(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def run_redpajama():
    prompt = input("Enter your prompt for RedPajama: ")
    result = query(prompt)
    output = result[0]['generated_text']

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_path = os.path.join(OUTPUT_DIR, "redpajama_response.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ RedPajama response saved at: {file_path}")
