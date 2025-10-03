# tts.py
import os
import requests
from dotenv import load_dotenv
import base64

load_dotenv()
API_TOKEN = os.getenv("HF_TOKEN")  # keep this name consistent with your .env
if not API_TOKEN:
    raise RuntimeError("HF_TOKEN not set. Add HF_TOKEN=hf_xxx to your .env")

# model URL (change if you prefer another TTS HF model)
API_URL = "https://api-inference.huggingface.co/models/speechbrain/tts-tacotron2-ljspeech"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

OUTPUT_DIR = "outputs"
DEFAULT_FILENAME = "output.wav"

def _save_bytes_to_file(b: bytes, filename: str) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "wb") as f:
        f.write(b)
    return path

def text_to_speech(text: str, filename: str = DEFAULT_FILENAME) -> str:
    """
    Sends text to the HF TTS model, decodes whatever the API returns
    (raw bytes or JSON-with-base64) and saves a real audio file.
    Returns the saved file path.
    """
    print("--- DEBUG ---")
    print(f"API URL: {API_URL}")
    print(f"Headers: {HEADERS}")
    print("-------------")
    
    payload = {"inputs": text}
    resp = requests.post(API_URL, headers=HEADERS, json=payload)

    if resp.status_code != 200:
        # show helpful debugging information
        raise RuntimeError(f"TTS request failed ({resp.status_code}): {resp.text}")

    content_type = resp.headers.get("content-type", "")

    # If JSON, look for base64 audio inside it
    if "application/json" in content_type or resp.text.strip().startswith("{"):
        data = resp.json()
        if "error" in data:
            raise RuntimeError(f"TTS API error: {data['error']}")

        # Common keys that may contain base64 audio
        possible_keys = ("audio", "wav", "data", "speech")
        audio_b64 = None
        for k in possible_keys:
            if k in data and isinstance(data[k], str):
                audio_b64 = data[k]
                break

        # fallback: try to find the first string in nested structure
        if audio_b64 is None:
            def find_first_string(obj):
                if isinstance(obj, str):
                    return obj
                if isinstance(obj, dict):
                    for v in obj.values():
                        s = find_first_string(v)
                        if s: return s
                if isinstance(obj, list):
                    for item in obj:
                        s = find_first_string(item)
                        if s: return s
                return None
            audio_b64 = find_first_string(data)

        if not audio_b64:
            raise RuntimeError(f"Could not find base64 audio in JSON response: {data}")

        # If it's a data URI "data:audio/wav;base64,AAAA...", strip prefix
        if audio_b64.startswith("data:"):
            audio_b64 = audio_b64.split(",", 1)[1]

        audio_bytes = base64.b64decode(audio_b64)
        return _save_bytes_to_file(audio_bytes, filename)

    # Otherwise treat as raw bytes (wav/mp3) and save directly
    return _save_bytes_to_file(resp.content, filename)

def run_tts():
    """Called by main.py — interactive prompt and save to outputs/"""
    text = input("Enter text to convert into speech: ").strip()
    if not text:
        print("No text entered. Exiting.")
        return
    try:
        saved = text_to_speech(text)
        print(f"✅ Audio saved at: {saved}")
    except Exception as e:
        print("TTS failed:", e)
