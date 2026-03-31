from google import genai
import os
from dotenv import load_dotenv
import speech_recognition as sr
import edge_tts
import tempfile
import asyncio
import pygame
import time

load_dotenv()  # Load environment variables from .env file

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

history = []

SYSTEM_PROMPT = """You are a helpful ai voice assistant that name is 'sumit'. Speak in a refined, clear and engaging manner.
Keep responses to 2-3 sentences — no bullet points, no markdown.
Your answer will be spoken aloud so write in natural flowing sentences."""

def listen() -> str | None:
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 1.2

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
            print("Recognizing...")
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            print("no speech detected...")
            return None
    
    print("transcripting...")
    try :
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"stt service error: {e}")
        return None


def ask_gemini(user_text: str) -> str:
    conversation = SYSTEM_PROMPT + "\n\n"
    for turn in history:
        conversation += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n\n"
    conversation += f"User: {user_text}\nAssistant:"
 
    print("Thinking...")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation
    )
    answer = response.text.strip()
    print(f"Assistant: {answer}")
    return answer
 
 
# =============================================================================
#  3. TEXT TO SPEECH  (edge-tts)
# =============================================================================
 
def speak(text: str):
    async def _generate():
        communicate = edge_tts.Communicate(text, voice="en-US-JennyNeural")
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            tmp = f.name
        await communicate.save(tmp)
        return tmp
 
    print("Speaking...")
    tmp = asyncio.run(_generate())
 
    pygame.mixer.init()
    pygame.mixer.music.load(tmp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.quit()
    os.remove(tmp)
 
 
# =============================================================================
#  4. MAIN PIPELINE  (called by main.py)
# =============================================================================
 
def run_pipeline() -> dict:
    user_text = listen()
    if not user_text:
        return {"reply": "I didn't catch that. Please try again.", "heard": ""}
 
    answer = ask_gemini(user_text)
    speak(answer)
 
    history.append({"user": user_text, "assistant": answer})
    if len(history) > 10:
        history.pop(0)
 
    return {"reply": answer, "heard": user_text}
