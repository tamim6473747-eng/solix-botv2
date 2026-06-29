import logging

from telegram import Update
from telegram.ext import (
    Application,
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

# -------------------------
# Logging
# -------------------------
logging.basicConfig(
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger("Solix")


# -------------------------
# Error Handler
# -------------------------
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.exception("Bot error:", exc_info=context.error)

    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "❌ Something went wrong. Try again later."
            )
        except Exception:
            pass


# -------------------------
# Build Application
# -------------------------
def build_application() -> Application:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("trending", trending_command))
    app.add_handler(CommandHandler("search", search_command))
    app.add_handler(CommandHandler("token", token_command))

    app.add_error_handler(error_handler)

    return app


# -------------------------
# MAIN (FIXED - NO ASYNC)
# -------------------------
def main():
    application = build_application()

    logger.info("🚀 Solix Bot starting...")

    application.run_polling(
        drop_pending_updates=True,
        allowed_updates=Update.ALL_TYPES,
    )


if __name__ == "__main__":
    main()
