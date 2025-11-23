from openai import OpenAI
import re
import os
from typing import List
from config import Parameters

def get_completion(complete_prompt: str) -> str:
    """
    Send a message to the OpenAI API to get a response.
    """
    try:
        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            base_url=os.environ.get("OPENAI_BASE_URL")
        )
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