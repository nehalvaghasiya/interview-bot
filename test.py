import re

# Your text format questions
text_questions = """
1. Q1
2 Q2
Question 3: Q3
Question:4 Q4
"""

# Use regular expression to find the question part after the number and separator
question_list = re.findall(r'\d[.:\s]*(.*)', text_questions)

# Print the question list
print(question_list)

