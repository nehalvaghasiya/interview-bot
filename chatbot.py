import uuid
import streamlit as st
from dotenv import load_dotenv
from streamlit_chat import message
from utils import get_completion, get_questions
from config import Parameters

# Load environment variables from .env file
load_dotenv()

class InterviewBot:
    """
    Class representing the Interview chatbot.
    """

    def __init__(self) -> None:
        """
        Initialize the InterviewBot and its session state.
        """
        if 'questions' not in st.session_state:
            st.session_state['questions'] = []

        if 'answers' not in st.session_state:
            st.session_state['answers'] = []

        if 'interview_step' not in st.session_state:
            st.session_state['interview_step'] = 0

        self.session_state = st.session_state

    def prepare_questions(self) -> None:
        """
        Prepare the interview by generating questions from the OpenAI API and the job description.

        The method calls the get_completion function with a prompt formatted with the job description,
        then processes the returned string to extract individual questions. These questions are stored
        in the session state along with a unique identifier for each question.
        """
        concatenated_questions = get_completion(Parameters.QUESTIONS_PROMPT.format(job_description=Parameters.JOB_DESCRIPTION))

        questions = get_questions(concatenated_questions)

        self.session_state['questions'] = [(question, self._generate_uuid()) for question in questions]

    def ask_question(self) -> None:
        """
        Display the current question.
        """
        text, key = self.session_state['questions'][self.session_state['interview_step']]
        message(text, key=key)

    def get_answer(self) -> None:
        """
        Get and store the answer provided by the user.
        """
        answer = st.text_input("Your answer: ", key="input" + str(self.session_state['interview_step']))

        if answer:
            self.session_state['answers'].append((answer, self._generate_uuid()))
            self.session_state['interview_step'] += 1
            st.rerun()

    def display_past_questions_and_answers(self) -> None:
        """
        Display all past questions and their corresponding answers.
        """
        for i in range(self.session_state['interview_step']):
            question_text, question_key = self.session_state['questions'][i]
            message(question_text, key=question_key)

            if i < len(self.session_state['answers']):
                answer_text, answer_key = self.session_state['answers'][i]
                message(answer_text, is_user=True, key=answer_key)

    def evaluate_candidate(self) -> str:
        """
        Generate an evaluation for the candidate based on their answers to the interview questions.
        """
        interview_text = "".join([f"Question: {question}\nAnswer: {answer}\n" for (question, _), (answer, _) in zip(self.session_state['questions'], self.session_state['answers'])])
        
        response = get_completion(Parameters.EVALUATION_PROMPT.format(job_description=Parameters.JOB_DESCRIPTION, interview_text=interview_text))

        return response

    def execute_interview(self) -> None:
        """
        Execute the interview process.

        This method manages the interview process by displaying past questions and their corresponding answers, 
        asking the current question, getting the answer from the candidate, and finally evaluating the candidate 
        when all questions have been answered. If the interview is complete, the candidate's responses are evaluated 
        using the OpenAI API, and the evaluation is displayed.
        """
        self.display_past_questions_and_answers()

        if self.session_state['interview_step'] < len(self.session_state['questions']):
            self.ask_question()
            self.get_answer()

        elif self.session_state['interview_step'] == len(self.session_state['questions']):
            evaluation = self.evaluate_candidate()
            st.write(f"OpenAI GPT-3.5's evaluation: {evaluation}")
            self.session_state['interview_step'] += 1

    @staticmethod
    def _generate_uuid() -> str:
        """
        Generate a unique identifier.
        """
        return str(uuid.uuid4())


def create_bot() -> None:
    """
    Create an InterviewBot and manage its operation.
    """
    bot = InterviewBot()

    if len(bot.session_state['questions']) == 0:
        message("Hello! I'm your interviewer bot powered by OpenAI. I will ask you a few questions, and your responses will be evaluated. Let's get started.", key="greeting")
        bot.prepare_questions()

    bot.execute_interview()


st.title("InterviewBot - AI Interview Chatbot")
create_bot()
