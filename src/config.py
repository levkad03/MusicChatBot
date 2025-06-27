import os

from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GENIUS_API_KEY = os.getenv("GENIUS_API_KEY")
