from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from services.dexscreener import get_token_by_address
from utils.formatters import format_token_details


async def token_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if not context.args:
        await update.message.reply_text(
            "❌ Please provide a contract address.\n"
            "Example: /token So11111111111111111111111111111111111111112"
        )
        return

    address = context.args[0]

    msg = await update.message.reply_text(
        "🪙 Fetching token details..."
    )

    try:
        token = await get_token_by_address(address)

        text = format_token_details(token)

        await msg.edit_text(
            text=text,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )

    except Exception:
        await msg.edit_text(
            "❌ Failed to fetch token details. Try again later."
      )
