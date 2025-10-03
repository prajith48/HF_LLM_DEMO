import requests, os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-small"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

OUTPUT_DIR = "outputs"

def stt(audio_file):
    with open(audio_file, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def run_stt():
    audio_file = input("Enter path of audio file (.wav): ")
    result = stt(audio_file)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    transcript_file = os.path.join(OUTPUT_DIR, "transcript.txt")
    with open(transcript_file, "w", encoding="utf-8") as f:
        f.write(result['text'])

    print(f"✅ Transcript saved at: {transcript_file}")
