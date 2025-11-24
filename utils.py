from openai import OpenAI
import re
import os
from typing import List
from config import Parameters

def get_llm_client() -> OpenAI:
    """
    Get the appropriate LLM client based on the provider configuration.
    Supports both OpenAI and Ollama.
    """
    provider = os.environ.get("LLM_PROVIDER", "openai").lower()
    
    if provider == "ollama":
        return OpenAI(
            api_key=os.environ.get("OLLAMA_API_KEY", "ollama"),
            base_url=os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434/v1")
        )
    else:
        # Default to OpenAI
        return OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            base_url=os.environ.get("OPENAI_BASE_URL")
        )

def get_completion(complete_prompt: str) -> str:
    """
    Send a message to the LLM API (OpenAI or Ollama) to get a response.
    """
    try:
        client = get_llm_client()
        messages = [{"role": "user", "content": complete_prompt}]
        response = client.chat.completions.create(
            model=Parameters.MODEL,
            messages=messages,
            temperature=0
        )
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Encountered an error: {e}")
        return f"Error: {str(e)}"


def get_questions(text_questions: str) -> List[str]:
    """
    Extract all questions from the concatenated_questions string using regular expressions
    """
    question_list = re.findall(r'\d[.:\s]*(.*)', text_questions)
    return question_list