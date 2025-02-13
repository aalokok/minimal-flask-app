# Dreamscape: Jungian Dream Analysis with AI

A web application that performs Jungian dream analysis using GPT-4 and generates dream-inspired artwork using DALL-E 3.

## Features

- Dream interpretation using Jungian psychology principles
- AI-generated artistic visualization of dreams
- Modern, avant-garde interface design
- Real-time analysis and image generation

## Live Demo

Visit [Dreamscape](https://cart498a4.onrender.com/)

## Technical Stack

- Flask (Python web framework)
- OpenAI GPT-4 (text analysis)
- DALL-E 3 (image generation)
- HTML/CSS (frontend)

## Deployment on Render.com

### Manual Setup

1. Create a new Web Service on Render
2. Link to your GitHub repository
3. Add Environment Variables:
   - `OPENAI_API_KEY`: Your OpenAI API key

### Build Commands
```bash
pip install flask
pip install openai
pip install python-dotenv
pip install gunicorn
```

### Start Command
```bash
gunicorn app:app
```

## Local Development

1. Clone the repository
2. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-key-here
   ```
3. Install dependencies manually:
   ```bash
   pip install flask openai python-dotenv
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Visit `http://127.0.0.1:5000` in your browser

## Project Structure
```
/
├── app.py              # Main Flask application
├── .env               # Environment variables (not in repo)
└── templates/
    └── index.html     # Frontend template
```

## Contributing

