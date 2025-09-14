from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY")

# https://console.groq.com/docs/models


ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192",
    "llama-3.3-70b-versatile"

]

settings = Settings()

