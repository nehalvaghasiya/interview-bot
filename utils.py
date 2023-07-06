import openai
import re
# openai.api_key = ''

def get_completion(complete_prompt: str, model="gpt-3.5-turbo") -> str:
    messages = [{"role": "user", "content": complete_prompt}]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages,
                                            temperature = 0)
    #time.sleep(5)
    return response.choices[0].message["content"]


def get_questions(text_questions):
    # question_list = [line.split('. ')[1] for line in text.split('\n') if line.strip() != '']
    question_list = re.findall(r'\d[.:\s]*(.*)', text_questions)
    return question_list