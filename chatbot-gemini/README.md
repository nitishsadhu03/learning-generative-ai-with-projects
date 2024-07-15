# Chatbot Project

This project is a chatbot implementation using LangChain with the Gemini API for natural language processing and Streamlit for a quick frontend.

## Overview

The chatbot leverages the power of LangChain to handle conversational flows, the Gemini API for advanced NLP capabilities, and Streamlit to create an interactive web interface for users.

## Features

- **Conversational AI**: Utilizes LangChain to manage and respond to user inputs.
- **NLP Integration**: Incorporates the Gemini API for natural language understanding and processing.
- **Interactive Frontend**: Streamlit provides a user-friendly interface for interacting with the chatbot.

## Setup Instructions

Follow the steps below to set up and run the chatbot project.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/nitishsadhu03/learning-generative-ai-with-projects.git
    cd learning-generative-ai-with-projects/chatbot
    ```

2. **Set up the virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**

    Create a `.env` file in the `chatbot` directory and add your Gemini API key:

    ```env
    GEMINI_API_KEY=your_gemini_api_key_here
    LANGCHAIN_API_KEY=your_langsmith_api_key_here
    LANGCHAIN_PROJECT=your_project_title_here
    ```

### Running the Chatbot

1. **Start the Streamlit app:**

    ```bash
    streamlit run main.py
    ```

2. **Open your browser** and navigate to `http://localhost:8501` to interact with the chatbot.
