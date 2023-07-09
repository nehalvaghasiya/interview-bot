import openai
import re
from typing import List
from openai.error import InvalidRequestError
from config import Parameters

def get_completion(complete_prompt: str) -> str:
    """
    Send a message to the OpenAI API to get a response.
    """
    try:
        messages = [{"role": "user", "content": complete_prompt}]
        response = openai.ChatCompletion.create(model=Parameters.MODEL, messages=messages,
                                                temperature = 0)
        return response.choices[0].message["content"]
    
    except InvalidRequestError as e:
        print(f"Encountered an error: {e}")
        return "Error: Input too long for model."


def get_questions(text_questions: str) -> List[str]:
    """
    Extract all questions from the concatenated_questions string using regular expressions
    """
    question_list = re.findall(r'\d[.:\s]*(.*)', text_questions)
    return question_list