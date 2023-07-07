import openai
import re
from typing import List
# openai.api_key = ''

def get_completion(complete_prompt: str, model="gpt-3.5-turbo") -> str:
    # Send a message to the OpenAI API to get a response
    messages = [{"role": "user", "content": complete_prompt}]
    response = openai.ChatCompletion.create(model=model, messages=messages,
                                            temperature = 0)
    #time.sleep(5)
    return response.choices[0].message["content"]


def get_questions(text_questions: str) -> List[str]:
    # Extract all questions from the text using regular expressions
    question_list = re.findall(r'\d[.:\s]*(.*)', text_questions)
    return question_list