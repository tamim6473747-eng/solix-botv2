import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN environment variable is missing."
    )

DEX_API_BASE = "https://api.dexscreener.com/latest/dex"

REQUEST_TIMEOUT = 20

MAX_RESULTS = 10

DEFAULT_HEADERS = {
    "User-Agent": "SolixTelegramBot/2.0",
    "Accept": "application/json",
}
