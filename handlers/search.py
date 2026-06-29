from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from services.dexscreener import search_tokens
from utils.formatters import format_search_results


async def search_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    query = " ".join(context.args)

    if not query:
        await update.message.reply_text(
            "❌ Please provide a token name or symbol.\n"
            "Example: /search bonk"
        )
        return

    msg = await update.message.reply_text(
        f"🔎 Searching for: {query}..."
    )

    try:
        tokens = await search_tokens(query)

        text = format_search_results(tokens)

        await msg.edit_text(
            text=text,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )

    except Exception:
        await msg.edit_text(
            "❌ Search failed. Try again later."
      )
