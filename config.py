import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Parameters:
    """
    Configurable parameters for the application.
    """

    # Determine which provider to use
    PROVIDER = os.environ.get("LLM_PROVIDER", "openai").lower()
    
    # Set model based on provider
    if PROVIDER == "ollama":
        MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")
    else:
        MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    QUESTIONS_PROMPT = "Job description: {job_description}\nBased on the given job description, kindly formulate five relevant interview questions with max 20 words each. These questions should aim to assess the candidate's competency for the job role. Ask one question at a time. Do not generate unnecessary texts except the questions. "
    
    EVALUATION_PROMPT = """
                        Job description: {job_description}

                        Question-Answers:\n{interview_text}

                        As an AI interview assistant, your task is to evaluate the quality and depth of the candidate's responses. Consider the following:

                        Does the candidate provide detailed answers that demonstrate their understanding and expertise?
                        Can you find tangible examples in their responses that relate to the job description?
                        Does the candidate elaborate on how they have used necessary skills or experiences to overcome challenges or achieve results?
                        Do the responses suggest the candidate has the ability to perform well in the role's complexities and challenges?
                        If the candidate's responses are inadequate, vague, or don't clearly demonstrate the needed skills or experiences, they may not be a suitable match for the role. In such cases, tactfully communicate this by saying: "Thank you for your responses. However, based on the answers provided, it appears there may be a misalignment with the requirements of the role we're seeking to fill. At this time, we cannot extend an offer. We appreciate your time and effort and wish you the best in your future endeavors."

                        If the responses indicate a strong fit for the role, then acknowledge the candidate's suitability by saying: "Thank you for your thoughtful responses. Based on your answers, it appears that your skills, experience, and understanding align well with the requirements of the role. We will be in touch with the next steps."
                        """    
    
    JOB_DESCRIPTION = """
                        Job description of advertised OpenAI Technical Expert / Data Scientist position:

                        TASKS:
                        Development and implementation of Machine Learning / Artificial Intelligence models for applications, e.g. in the area of Natural Language Processing or Computer Vision, with a focus on OpenAI technologies to improve our services and processes

                        Collaborate closely with other Data Scientists, subject matter experts, and external service providers

                        Use case-based evaluation and consulting on the use of analytical methods and approaches (especially OpenAI technologies) to improve our processes and services

                        Collaborate closely with our business units as an internal development partner, supporting them from the ideation phase to implementation

                        QUALIFICATIONS:
                        Master in computer science, mathematics, physics or a comparable qualification with a focus on Machine Learning / AI.

                        At least three years of experience in implementing Machine Learning / AI models, including the use of OpenAI technologies

                        In-depth expertise in the area of current Machine Learning / AI methods, especially Large Language Models

                        Comprehensive knowledge of relevant programming languages, including Python

                        Experience with cloud computing platforms, preferably Azure

                        Knowledge of natural language processing and/or computer vision

                        Strong analytical skills and the ability to solve complex problems

                        Strong English communication skills are required, and basic knowledge of German is preferred
                        """