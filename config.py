import os
from dotenv import load_dotenv

# Load .env locally (Render এ ignore হবে)
load_dotenv()

# -------------------------
# BOT TOKEN (Required)
# -------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError(
        "❌ BOT_TOKEN is missing! Set it in environment variables."
    )

# -------------------------
# DexScreener API Config
# -------------------------
DEX_API_BASE = "https://api.dexscreener.com/latest/dex"

# -------------------------
# Request Settings
# -------------------------
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "20"))

# max results fallback
MAX_RESULTS = int(os.getenv("MAX_RESULTS", "10"))

# -------------------------
# Headers (API safety)
# -------------------------
DEFAULT_HEADERS = {
    "User-Agent": os.getenv(
        "USER_AGENT",
        "SolixTelegramBot/2.0"
    ),
    "Accept": "application/json",
}
