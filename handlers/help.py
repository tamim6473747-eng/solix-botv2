from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    help_text = (
        "📚 <b>Solix Help</b>\n\n"
        "<b>Commands</b>\n\n"
        "🏠 <b>/start</b>\n"
        "Show the welcome message.\n\n"
        "🔥 <b>/trending</b>\n"
        "Display the latest trending Solana tokens.\n\n"
        "🔎 <b>/search &lt;keyword&gt;</b>\n"
        "Search for a token by name, symbol, or address.\n"
        "Example:\n"
        "<code>/search bonk</code>\n\n"
        "🪙 <b>/token &lt;contract_address&gt;</b>\n"
        "Get detailed information about a token.\n"
        "Example:\n"
        "<code>/token So11111111111111111111111111111111111111112</code>\n\n"
        "ℹ️ <b>Data Source</b>\n"
        "DexScreener API (latest)"
    )

    await update.message.reply_text(
        text=help_text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )
