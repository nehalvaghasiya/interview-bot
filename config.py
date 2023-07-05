class Parameters:
    questions_prompt = "Job description: {job_description}\nBased on the given job description, kindly formulate two relevant interview questions with max 20 words each. These questions should aim to assess the candidate's competency for the job role. Ask one question at a time. Do not generate unnecessary texts except the questions. "
    evaluation_prompt =  """Job description: {job_description}\n\nQuestion-Answers:\n{interview_text}\n\nAs an AI interview assistant, you have been tasked to evaluate the candidate's responses. Based on the answers provided, determine whether the candidate is suitable for the role specified in the job description. Bear in mind to gauge the authenticity and completeness of their responses. If any inaccuracies or significant omissions are observed, you have to reject the candidate tactfully and you have to say the words "Sorry, we can not hire you.", ensuring your communication remains courteous and respectful. """
    job_description = """
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