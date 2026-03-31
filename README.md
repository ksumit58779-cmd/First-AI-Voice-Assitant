# First-AI-Voice-Assitant
A normal voice assistant that tells everything you need 


## how to make?
This is very good thing to make if your intereted about tech and ai. 

### First of all this is file structure
your-project/
├── templates/
│   └── index.html     ← cream mic UI
├── app.py             ← STT + Gemini + TTS logic
├── main.py            ← Flask routes, connects everything
└── .env               ← GEMINI_API_KEY=your-key-here

most important thing i always said don't waste your money for buying expensive api_key you just need a simple api key like gemini or you can use 
ollama this is very simple and local ai tool , you can intergate in this project.

well after save your gemini api key in .env build app.py where we make tts logic , function and connect gemini in your local server. this whole structure like how exactly this file works --
your ask anything -> messages goes -> gemini generate text -> then its convert into voice 

that's it . then connect everything in one file main.py , use flask library for run this thing in local server but first of all create your ui , i already make for you but you can change and make something different using claude for building powerful ui. 
⚠️ Make sure in app.py where you add system prompt add your name or add any ai voice assistant name you want to add , i add my name "sumit" you can addd whatever you want 


That's it your first ai voice assistant is ready, yes this is not extraordinary but its simple and give you basic of how to make a simple ai voice assistant 
