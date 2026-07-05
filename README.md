# AI Video Assistant

AI Video Assistant is an AI-powered meeting intelligence application built with Streamlit. It can summarize meetings from YouTube videos or local audio/video recordings, extract actionable insights, and let users ask questions about the transcript in a conversational way.

This project demonstrates the practical use of AI in real-world workflows such as meeting analysis, documentation, and knowledge retrieval.

## Key Features
- Process YouTube video links and local recording files
- Convert audio/video into a transcribed text format
- Generate a professional meeting summary
- Extract action items, key decisions, and open questions
- Enable chat-style Q&A over the meeting transcript using a retrieval-based approach

## Tech Stack
- Python
- Streamlit
- Whisper
- PyDub
- LangChain
- Mistral AI
- Chroma / vector search

## Project Structure
- app.py – Streamlit web application
- core/ – transcription, summarization, extraction, and RAG logic
- utils/audio_processor.py – audio/video preprocessing pipeline
- tests/ – regression tests for the pipeline

## How It Works
1. The app accepts either a YouTube URL or a local file path.
2. Audio is downloaded or read from the provided source.
3. The content is converted into chunks and transcribed.
4. The transcript is used to generate:
   - summary
   - action items
   - key decisions
   - follow-up questions
   - conversational answers

## Installation
1. Clone the repository
   ```bash
   git clone https://github.com/rishiraj55200/AI-Video-Assistant.git
   cd AI-Video-Assistant
   ```
2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install dependencies
   ```bash
   pip install -r Requirements.txt
   ```
4. Create a .env file with your Mistral API key
   ```env
   MISTRAL_API_KEY=your_key_here
   ```

## Run Locally
```bash
streamlit run app.py
```

## Usage
- Open the local Streamlit URL in your browser
- Paste a YouTube URL or enter the path to a local recording
- Click Analyse to generate insights from the content

## Why This Project Is Valuable
This project highlights skills in:
- AI application development
- NLP and speech-to-text workflows
- LLM-based summarization and extraction
- Building interactive user interfaces
- End-to-end software development for practical use cases

## Notes
- For local files, provide the absolute path to the recording
- The app includes fallback logic so it can still generate basic structured output if the AI service is temporarily unavailable
