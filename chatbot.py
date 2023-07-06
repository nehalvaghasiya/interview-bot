import uuid
import streamlit as st
from streamlit_chat import message
from utils import get_completion, get_questions
from config import Parameters

class InterviewBot:
    def __init__(self):
        if 'questions' not in st.session_state:
            st.session_state['questions'] = []

        if 'answers' not in st.session_state:
            st.session_state['answers'] = []

        if 'interview_step' not in st.session_state:
            st.session_state['interview_step'] = 0

    def conduct_interview(self):
        text_questions = get_completion(Parameters.questions_prompt.format(job_description=Parameters.job_description))
        questions = get_questions(text_questions)
        for question in questions:
            st.session_state['questions'].append((question, str(uuid.uuid4())))

    def ask_question(self):
        text, key = st.session_state['questions'][st.session_state['interview_step']]
        message(text, key=key)

    def get_answer(self):
        answer = st.text_input("Your answer: ", key="input" + str(st.session_state['interview_step']))
        if answer:
            st.session_state['answers'].append((answer, str(uuid.uuid4())))
            st.session_state['interview_step'] += 1
            st.experimental_rerun()

    def display_past_questions_and_answers(self):
        for i in range(st.session_state['interview_step']):
            question_text, question_key = st.session_state['questions'][i]
            message(question_text, key=question_key)
            if i < len(st.session_state['answers']):
                answer_text, answer_key = st.session_state['answers'][i]
                message(answer_text, is_user=True, key=answer_key)

    def evaluate_candidate(self):
        # Combine the questions and answers into a single string
        interview_text = ""
        
        for (question, _), (answer, _) in zip(st.session_state['questions'], st.session_state['answers']):
            interview_text += f"Question: {question}\nAnswer: {answer}\n"
      
        # Use the OpenAI API to generate a response
        response = get_completion(Parameters.evaluation_prompt.format(job_description=Parameters.job_description, interview_text=interview_text))

        return response

# Creating the chatbot interface
st.title("InterviewBot")

bot = InterviewBot()

# Only conduct the interview once, when the application first starts
if len(st.session_state['questions']) == 0:
    message("Hello! I'm your interviewer bot powered by OpenAI. I will ask you a few questions, and your responses will be evaluated. Let's get started.", key="greeting")
    bot.conduct_interview()

bot.display_past_questions_and_answers()

if st.session_state['interview_step'] < len(st.session_state['questions']):
    bot.ask_question()
    bot.get_answer()
elif st.session_state['interview_step'] == len(st.session_state['questions']):
    evaluation = bot.evaluate_candidate()
    st.write(f"OpenAI GPT-3.5's evaluation: {evaluation}")
    st.session_state['interview_step'] += 1
