# Restaurant Name and Menu Generator

This project leverages LangChain and the Gemini API to generate creative restaurant names and menu items based on a selected cuisine.

## Overview

Users can select a cuisine from a dropdown menu, and the model will generate a fancy name for a restaurant with that cuisine, along with some menu items related to that cuisine.

## Features

- **Cuisine Selection**: Users can choose a cuisine from a dropdown menu.
- **Creative Name Generation**: Generates a fancy name for a restaurant based on the selected cuisine.
- **Menu Item Generation**: Provides a list of menu items related to the chosen cuisine.

## Setup Instructions

Follow the steps below to set up and run the chatbot project.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/nitishsadhu03/learning-generative-ai-with-projects.git
    cd learning-generative-ai-with-projects/restaurant-generator
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

2. **Open your browser** and navigate to `http://localhost:8501` to use the application.

## Project Structure

- `main.py`: The main script for running the application.
- `requirements.txt`: Lists the dependencies required to run the project.
- `.env`: Environment variables file (not included in the repository).
- `venv/`: Virtual environment directory (not included in the repository).
