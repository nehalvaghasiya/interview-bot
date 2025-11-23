# AI Interview Chatbot

## Table of Contents

- [Overview](#overview)
- [Technical Aspect](#technical-aspect)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Directory Tree](#directory-tree)
- [Troubleshooting](#troubleshooting)
- [Bug / Feature Request](#bug--feature-request)
- [Technologies Used](#technologies-used)

## Overview

This project is an AI Interview Chatbot that uses OpenAI's GPT models (GPT-4o-mini by default) and the Streamlit framework. The chatbot generates job-specific interview questions and evaluates candidate responses using advanced language model capabilities.


https://github.com/nehalvaghasiya/interview-bot/assets/78668871/514c7ac2-c2e8-4e60-a4f4-2dd76bd30edd


## Technical Aspect

The Interview Chatbot project consists of three main components:

1. **Question Generation**: Creates job-specific interview questions based on a configurable job description
2. **Response Collection**: Interactive chat interface for collecting candidate answers
3. **Evaluation**: AI-powered assessment of candidate responses against job requirements

The project uses OpenAI's API with support for custom base URLs, making it compatible with OpenAI-compatible endpoints.

## Installation

### Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip

### Setup Environment Variables

1. Copy the `.env.example` file to create your own `.env` file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file with your OpenAI API credentials:
   ```env
   OPENAI_API_KEY=your_actual_api_key_here
   OPENAI_BASE_URL=https://api.openai.com/v1
   OPENAI_MODEL=gpt-4o-mini
   ```
   
   - Replace `your_actual_api_key_here` with your actual OpenAI API key
   - Update `OPENAI_BASE_URL` if using a custom OpenAI-compatible endpoint
   - Change `OPENAI_MODEL` to use a different model (e.g., `gpt-4`, `gpt-4-turbo`)

### Installation Methods

#### Method 1: Using uv (Recommended)

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/nehalvaghasiya/interview-bot.git
cd interview-bot

# Install dependencies using uv
uv sync

# Activate the virtual environment
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows

# Run the application
streamlit run chatbot.py
```

#### Method 2: Using uv with requirements.txt

```bash
# Create a virtual environment and install dependencies
uv venv
source .venv/bin/activate  # Linux/Mac
uv pip install -r requirements.txt

# Run the application
streamlit run chatbot.py
```

#### Method 3: Using pip

```bash
# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run chatbot.py
```

## Usage

1. **Start the application**:
   ```bash
   streamlit run chatbot.py
   ```

2. **Access the chatbot**: Open your browser at `http://localhost:8501`

3. **Interact with the bot**:
   - The chatbot will greet you and begin asking interview questions
   - Type your answers in the text input field
   - Press Enter to submit each answer
   - After all questions are answered, you'll receive an AI-generated evaluation

## Configuration

### Customizing the Job Description

Edit `config.py` to customize the job description and prompts:

```python
class Parameters:
    MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    
    JOB_DESCRIPTION = """
    Your custom job description here...
    """
    
    # Customize prompts as needed
    QUESTIONS_PROMPT = "..."
    EVALUATION_PROMPT = "..."
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `OPENAI_BASE_URL` | API base URL | `https://api.openai.com/v1` |
| `OPENAI_MODEL` | Model to use | `gpt-4o-mini` |

## Examples

### Example Interview Flow

1. **Bot**: "Hello! I'm your interviewer bot powered by OpenAI. I will ask you a few questions, and your responses will be evaluated. Let's get started."

2. **Bot**: "What is your experience with Machine Learning and AI implementation?"

3. **User**: "I have 5 years of experience implementing ML models in production..."

4. **Bot**: "Can you describe a challenging NLP project you've worked on?"

5. **User**: "I developed a sentiment analysis system for customer feedback..."

6. *(After all questions)*

7. **Bot**: "Thank you for your thoughtful responses. Based on your answers, it appears that your skills, experience, and understanding align well with the requirements of the role..."

## Directory Tree

```
interview-bot/
├── .env.example              # Environment variables template
├── .github/                  # GitHub configuration
├── .gitignore               # Git ignore rules
├── README.md                # This file
├── chatbot.py               # Main Streamlit application
├── config.py                # Configuration and prompts
├── utils.py                 # Utility functions (API calls, text processing)
├── pyproject.toml           # Project metadata and dependencies (uv)
├── requirements.txt         # Python dependencies (pip)
├── uv.lock                  # Locked dependencies (uv)
├── devtools/                # Development tools
│   └── lint.py
├── images/                  # Project images
│   ├── openai.png
│   └── streamlit.jpg
├── src/                     # Source package (if using as package)
│   └── interview_bot.egg-info/
└── tests/                   # Test files
    └── test_placeholder.py
```

## Troubleshooting

### Common Issues

#### Module Not Found Errors

If you encounter import errors:

```bash
# Ensure you're in the virtual environment
source .venv/bin/activate  # Linux/Mac

# Reinstall dependencies
uv pip install -r requirements.txt
# or
pip install -r requirements.txt
```

#### API Connection Errors

- Verify your `.env` file exists and contains valid credentials
- Check that `OPENAI_API_KEY` is set correctly
- Ensure `OPENAI_BASE_URL` is accessible from your network

#### Model Not Found Error

If you get a "model not found" error:
- Update the `OPENAI_MODEL` in your `.env` file to a model available in your account
- Common models: `gpt-4o-mini`, `gpt-4o`, `gpt-4-turbo`, `gpt-4`

#### Streamlit Errors

If Streamlit throws errors:
```bash
# Clear Streamlit cache
streamlit cache clear

# Restart the application
streamlit run chatbot.py
```

### Getting Help

If issues persist:
1. Check that all dependencies are correctly installed
2. Verify Python version is 3.11 or higher: `python --version`
3. Review error logs in the terminal
4. Open an issue on GitHub with error details

## Bug / Feature Request

If you find a bug or the chatbot doesn't work as expected, please open an issue [here](https://github.com/nehalvaghasiya/interview-bot/issues/new) with:
- Description of the issue
- Steps to reproduce
- Error messages or screenshots
- Your environment details (OS, Python version)

If you'd like to request a new feature, open an issue [here](https://github.com/nehalvaghasiya/interview-bot/issues/new) with:
- Feature description
- Use case and benefits
- Example scenarios

## Technologies Used

<img src="images/openai.png" width="125"/><img src="images/streamlit.jpg" width="210"/> 

- **OpenAI API** - GPT-4o-mini and other models for question generation and evaluation
- **Streamlit** - Web framework for the interactive chat interface
- **Python-dotenv** - Environment variable management
- **uv** - Fast Python package manager
