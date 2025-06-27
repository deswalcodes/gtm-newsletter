# llm/summarizer.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text, max_tokens=150):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You're a newsletter assistant. Summarize technical content in 3 bullet points.",
                },
                {"role": "user", "content": text}
            ],
            temperature=0.5,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error]: {str(e)}"

# Example usage
if __name__ == "__main__":
    sample_text = """
    Whisper is an automatic speech recognition (ASR) system trained on 680,000 hours of multilingual and multitask supervised data collected from the web.
    The resulting models demonstrate robust zero-shot performance on many datasets without the need for fine-tuning.
    """
    print(summarize_text(sample_text))
