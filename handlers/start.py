from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    text = (
        "🚀 <b>Welcome to Solix</b>\n\n"
        "Your Solana token discovery bot powered by DexScreener.\n\n"
        "<b>Available Commands</b>\n"
        "• /trending - View trending Solana tokens\n"
        "• /search <token name> - Search tokens\n"
        "• /token <contract address> - View token details\n"
        "• /help - Show help menu\n\n"
        "Example:\n"
        "<code>/search bonk</code>\n"
        "<code>/token So11111111111111111111111111111111111111112</code>"
    )

    await update.message.reply_text(
        text=text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )
