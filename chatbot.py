import openai
from utils import get_completion, get_questions
from config import Parameters



class InterviewBot:
    def __init__(self):
        self.answers = []
        self.questions= []
    
    def conduct_interview(self):
        text_questions = get_completion(Parameters.questions_prompt.format(job_description=Parameters.job_description))
        questions = get_questions(text_questions)
        for question in questions:
            self.ask_question(question)

    def ask_question(self, question):
        print(question)
        answer = input()
        self.answers.append(answer)

    def evaluate_candidate(self):

        # Combine the questions and answers into a single string
        interview_text = ""
        
        for question, answer in zip(self.questions, self.answers):
            interview_text += f"Question: {question}\nAnswer: {answer}\n"
      
        # Use the OpenAI API to generate a response
        response = get_completion(Parameters.evaluation_prompt.format(job_description=Parameters.job_description, interview_text=interview_text))

        return response

questions = [
    "What is your educational background?",
    "Do you have experience in implementing Machine Learning / AI models?",
    "What is your expertise in the area of current Machine Learning / AI methods?",
    "Do you have comprehensive knowledge of Python?",
    "Do you have experience with cloud computing platforms, preferably Azure?",
    "Do you have knowledge of natural language processing and/or computer vision?",
    "Can you describe a situation where you used your analytical skills to solve a complex problem?",
    "How strong are your English communication skills?",
    "Do you have basic knowledge of German?",
]



bot = InterviewBot()
bot.conduct_interview()
evaluation = bot.evaluate_candidate()

print(f"GPT-3's evaluation: {evaluation}")
