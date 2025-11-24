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

2. **Choose your LLM provider** - Edit the `.env` file:

   **Option A: Using OpenAI**
   ```env
   LLM_PROVIDER=openai
   OPENAI_API_KEY=your_actual_api_key_here
   OPENAI_BASE_URL=https://api.openai.com/v1
   OPENAI_MODEL=gpt-4o-mini
   ```
   
   - Replace `your_actual_api_key_here` with your actual OpenAI API key
   - Update `OPENAI_BASE_URL` if using a custom OpenAI-compatible endpoint
   - Change `OPENAI_MODEL` to use a different model (e.g., `gpt-4`, `gpt-4-turbo`)

   **Option B: Using Ollama (Local/Free)**
   ```env
   LLM_PROVIDER=ollama
   OLLAMA_BASE_URL=http://localhost:11434/v1
   OLLAMA_MODEL=llama3.2
   OLLAMA_API_KEY=ollama
   ```
   
   - Install Ollama from [ollama.ai](https://ollama.ai)
   - Pull a model: `ollama pull llama3.2` (or `llama3.1`, `mistral`, `qwen2.5`, etc.)
   - Start Ollama: `ollama serve` (usually runs automatically)
   - Change `OLLAMA_MODEL` to any model you have pulled

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

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `LLM_PROVIDER` | LLM provider to use (`openai` or `ollama`) | `openai` | Yes |
| **OpenAI Settings** | | | |
| `OPENAI_API_KEY` | Your OpenAI API key | - | If using OpenAI |
| `OPENAI_BASE_URL` | OpenAI API base URL | `https://api.openai.com/v1` | No |
| `OPENAI_MODEL` | OpenAI model name | `gpt-4o-mini` | No |
| **Ollama Settings** | | | |
| `OLLAMA_BASE_URL` | Ollama API base URL | `http://localhost:11434/v1` | No |
| `OLLAMA_MODEL` | Ollama model name | `llama3.2` | No |
| `OLLAMA_API_KEY` | Placeholder (Ollama doesn't need real key) | `ollama` | No |

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

**For OpenAI:**
- Verify your `.env` file exists and contains valid credentials
- Check that `OPENAI_API_KEY` is set correctly
- Ensure `OPENAI_BASE_URL` is accessible from your network

**For Ollama:**
- Ensure Ollama is running: `ollama serve` (or check if it's running as a service)
- Verify the model is installed: `ollama list`
- Pull the model if missing: `ollama pull llama3.2`
- Check Ollama is accessible: `curl http://localhost:11434/api/tags`
- Verify `OLLAMA_BASE_URL` points to the correct endpoint

#### Model Not Found Error

**For OpenAI:**
- Update the `OPENAI_MODEL` in your `.env` file to a model available in your account
- Common models: `gpt-4o-mini`, `gpt-4o`, `gpt-4-turbo`, `gpt-4`

**For Ollama:**
- List available models: `ollama list`
- Pull the desired model: `ollama pull <model-name>`
- Popular models: `llama3.2`, `llama3.1`, `mistral`, `qwen2.5`, `phi3`
- Update `OLLAMA_MODEL` in `.env` to match an installed model

#### Ollama-Specific Issues

**Ollama not responding:**
```bash
# Check if Ollama is running
ps aux | grep ollama

# Start Ollama
ollama serve
```

**Slow responses with Ollama:**
- Local models require sufficient RAM and compute
- Consider using smaller models: `phi3`, `llama3.2:1b`
- Or faster models: `qwen2.5:3b`, `mistral`

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
- **Ollama** - Local LLM support (Llama 3.2, Mistral, Qwen, and more)
- **Streamlit** - Web framework for the interactive chat interface
- **Python-dotenv** - Environment variable management
- **uv** - Fast Python package manager

### Supported LLM Providers

#### OpenAI
- Cloud-based API
- High-quality responses
- Requires API key and costs per token
- Models: GPT-4o, GPT-4o-mini, GPT-4-turbo, GPT-3.5-turbo

#### Ollama
- Run models locally on your machine
- Free and private
- No internet required after model download
- Popular models: Llama 3.2, Llama 3.1, Mistral, Qwen 2.5, Phi-3
- Learn more: [ollama.ai](https://ollama.ai)

