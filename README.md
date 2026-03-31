# First-AI-Voice-Assitant

A normal voice assistant that tells everything you need.

## How to make?

This is very good thing to make if your interested about tech and AI.

### First of all this is file structure

```text
your-project/
├── templates/
│   └── index.html     ← cream mic UI
├── app.py             ← STT + Gemini + TTS logic
├── main.py            ← Flask routes, connects everything
└── .env               ← GEMINI_API_KEY=your-key-here
```

Most important thing I always said: don't waste your money for buying expensive API keys. You just need a simple API key like Gemini or you can use Ollama. This is a very simple and local AI tool, you can integrate it in this project.

Well after saving your Gemini API key in `.env`, build `app.py` where we make TTS logic, functions, and connect Gemini in your local server.

This whole structure is like this:

```text
you ask anything -> message goes -> Gemini generate text -> then it converts into voice
```

That's it.

Then connect everything in one file `main.py`. Use Flask library for running this thing in local server.

But first of all create your UI. I already made one for you, but you can change it and make something different using Claude for building a powerful UI.

⚠️ Make sure in `app.py` where you add system prompt, add your name or add any AI voice assistant name you want to add. I added my name "sumit" but you can add whatever you want.

That's it, your first AI voice assistant is ready. Yes, this
