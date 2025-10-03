from summarizer import run_summarizer
from mistral_llm import run_mistral
from redpajama_llm import run_redpajama
from tts import run_tts
from stt import run_stt

if __name__ == "__main__":
    print("1. Summarization")
    print("2. Mistral LLM")
    print("3. RedPajama LLM")
    print("4. Text-to-Speech")
    print("5. Speech-to-Text")
    
    choice = input("Choose option: ")

    if choice == "1":
        run_summarizer()
    elif choice == "2":
        run_mistral()
    elif choice == "3":
        run_redpajama()
    elif choice == "4":
        run_tts()
    elif choice == "5":
        run_stt()
    else:
        print("Invalid choice")
