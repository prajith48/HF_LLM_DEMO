# Hugging Face API Demo

A simple Python command-line application demonstrating how to use various Hugging Face Inference APIs for tasks like text summarization, large language model (LLM) interaction, text-to-speech (TTS), and speech-to-text (STT).

All generated outputs are saved in the `outputs/` directory.

## Features

*   **Text Summarization**: Condense long articles or text using the `facebook/bart-large-cnn` model.
*   **LLM Interaction**: Chat with large language models like `mistralai/Mistral-7B-v0.1` and `togethercomputer/RedPajama-INCITE-7B-Instruct`.
*   **Text-to-Speech (TTS)**: Convert text into a `.wav` audio file using the `speechbrain/tts-tacotron2-ljspeech` model.
*   **Speech-to-Text (STT)**: Transcribe an audio file into text using the `openai/whisper-small` model.

## Prerequisites

*   Python 3.7+
*   A Hugging Face account.
*   A Hugging Face User Access Token with `read` permissions. You can get one from your Hugging Face account settings.

## Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository

First, clone the project to your local machine (or simply use the existing files if you've already downloaded them).

```bash
git clone https://github.com/your-username/hf_llm_demo.git
cd hf_llm_demo
```

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

**On Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

The project requires a few Python packages. Create a file named `requirements.txt` in the project root with the following content:

**`requirements.txt`**
```
requests
python-dotenv
```

Now, install these packages using pip:
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

The application needs your Hugging Face API token to authenticate with the API.

1.  Create a file named `.env` in the root of the project directory.
2.  Add your API token to this file as shown below. Replace `hf_xxx...` with your actual token.

**`.env`**
```
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
> **Security Note:** The `.env` file should not be committed to version control. If you are using Git, add `.env` to your `.gitignore` file.

## Usage

Once the setup is complete, you can run the main application.

### Main Application

Run `main.py` to see a menu of available options:

```bash
python main.py
```

You will be prompted to choose a task:
```
1. Summarization
2. Mistral LLM
3. RedPajama LLM
4. Text-to-Speech
5. Speech-to-Text
Choose option:
```
Enter the number corresponding to the task you want to perform and follow the on-screen instructions.

### Connection Test Utility

If you encounter any connection errors, you can run the `debug_connection.py` script. This script makes a simple, direct request to the Hugging Face API to verify that your token and network connection are working correctly.

```bash
python debug_connection.py
```
A successful test will print `✅ SUCCESS`, confirming your environment is set up correctly. A failure will provide debugging information related to network, firewall, or authentication issues.

## Project Structure

```
.
├── outputs/                # Directory for all generated files (created automatically)
├── .env                    # Stores your Hugging Face API token (you create this)
├── requirements.txt        # Lists Python dependencies (you create this)
├── main.py                 # Main entry point for the application
├── summarizer.py           # Module for text summarization
├── mistral_llm.py          # Module for Mistral LLM
├── redpajama_llm.py        # Module for RedPajama LLM
├── tts.py                  # Module for Text-to-Speech
├── stt.py                  # Module for Speech-to-Text
└── debug_connection.py     # Utility to test API connectivity
```

---

## License

This project is licensed under the MIT License. See the text below for more details.

```
MIT License

Copyright (c) 2023 [Your Name or Organization]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```