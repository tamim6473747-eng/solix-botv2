from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from services.dexscreener import get_trending_tokens
from utils.formatters import format_trending_message


async def trending_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    msg = await update.message.reply_text(
        "📡 Fetching trending Solana tokens..."
    )

    try:
        tokens = await get_trending_tokens()

        if not tokens:
            await msg.edit_text(
                "⚠️ No trending data found right now."
            )
            return

        text = format_trending_message(tokens)

        await msg.edit_text(
            text=text,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )

    except Exception:
        await msg.edit_text(
            "❌ Failed to fetch trending tokens. Try again later."
      )
