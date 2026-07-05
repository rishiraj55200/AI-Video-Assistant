# AI Video Assistant

AI Video Assistant is a Streamlit-based application that helps you summarize meetings from YouTube videos or local audio/video recordings. It transcribes the media, generates a concise summary, extracts action items, key decisions, and open questions, and supports a chatbot-style Q&A over the transcript.

## Features
- Paste a YouTube video URL or provide a local file path
- Transcribe audio using Whisper/Sarvam-based workflow
- Generate a meeting summary
- Extract action items, key decisions, and follow-up questions
- Ask questions about the meeting transcript using a RAG-style chat experience

## Tech Stack
- Python
- Streamlit
- Whisper
- PyDub
- LangChain
- Mistral AI
- Chroma / vector search

## Project Structure
- app.py – Streamlit frontend
- core/ – summarization, transcription, extraction, and RAG logic
- utils/audio_processor.py – audio/video preprocessing
- tests/ – regression tests

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

## Run the App
```bash
streamlit run app.py
```

## Usage
- Open the local Streamlit URL in your browser
- Paste a YouTube URL or enter a local file path
- Click Analyse to generate the summary and insights

## Notes
- For local files, provide the absolute path to the audio/video file
- The app uses fallback logic if the AI service is unavailable, so it can still return basic structured output
