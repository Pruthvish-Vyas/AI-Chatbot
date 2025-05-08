# Simple AI Chat App

A streamlit-based chat application that allows users to interact with various AI models through different platforms, primarily focused on Together AI integration.

## Features

- Multi-platform support (Together AI, OpenAI, Hugging Face)
- Multiple model selection options
- Conversation memory management
- Past conversation storage and retrieval
- User-friendly interface with Streamlit
- Configurable output parameters

## Model Options

### Together AI
- Mistral-7B-Instruct-v0.1
- GPT-JT-6B-v1
- Llama-3.3-70B-Instruct-Turbo-Free
- DeepSeek-R1-Distill-Llama-70B-free
- Llama-Vision-Free

### OpenAI
- text-davinci-003
- gpt-3.5-turbo
- gpt-4

### Hugging Face
- bigscience/bloom
- facebook/opt-6.7b

## Installation

### Local Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd simple-ai-chat-app
```
2. Install required packages:

```
pip install -r requirements.txt
```
### Docker Installation

1. Build the docker image:
```
docker build -t app .
```

2. Run the container:
```
docker run -p 8501:8501 app
```



# Usage

### Running Locally

1. Run the application:
```
streamlit run app.py
```

2. Configure the settings in the sidebar:

- Select your preferred platform
- Choose an AI model
- Enter your API key
- Adjust max tokens if needed

3. Start chatting!

### Running with Docker
After starting the container,access the application at:

```
http://localhost:8501
```


# Project Structure:
```
Simple AI Chat App
│
├── Imports
│   ├── streamlit
│   └── langchain
│       ├── Together (LLM)
│       ├── ConversationChain
│       └── ConversationBufferMemory
│
├── Sidebar Settings
│   ├── Platform Selection
│   ├── API Key Input
│   └── Max Tokens Slider
│
├── Session State Management
│   ├── memory
│   ├── conversation
│   └── past_conversations
│
└── Main Chat Interface
    └── Chat Display
```
# Requirements
- Python 3.8+
- Streamlit
- LangChain
- Together AI API key (for Together AI models)
