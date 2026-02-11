import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Groq API
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Groq sozlamalari
GROQ_MODEL = "llama-3.3-70b-versatile"  # Yangi model
MAX_TOKENS = 2000
TEMPERATURE = 0.7

# Database
DATABASE_FILE = "data.json"

# Badge sozlamalari
BADGES = {
    1: "🎯 Boshlang'ich",
    5: "🔥 5 kun",
    10: "⭐ 10 kun",
    20: "💎 20 kun",
    30: "🏆 30 kun",
    50: "👑 50 kun",
    100: "🚀 100 kun"
}
