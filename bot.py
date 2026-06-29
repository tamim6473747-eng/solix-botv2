import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

from config import BOT_TOKEN

from handlers.start import start_command
from handlers.help import help_command
from handlers.trending import trending_command
from handlers.search import search_command
from handlers.token import token_command

logging.basicConfig(
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger("Solix")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.exception("Error:", exc_info=context.error)

    if isinstance(update, Update) and update.effective_message:
        await update.effective_message.reply_text(
            "❌ Error occurred. Try again later."
        )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("trending", trending_command))
    app.add_handler(CommandHandler("search", search_command))
    app.add_handler(CommandHandler("token", token_command))

    app.add_error_handler(error_handler)

    logging.info("🚀 Bot starting...")

    app.run_polling(
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()
