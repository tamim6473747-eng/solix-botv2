import asyncio
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
# Post Init
# -------------------------
async def post_init(application: Application):
    logger.info("===================================")
    logger.info("✅ Solix Telegram Bot Started")
    logger.info("===================================")


# -------------------------
# Error Handler
# -------------------------
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.exception("Unhandled exception:", exc_info=context.error)

    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "❌ Something went wrong. Please try again later."
            )
        except Exception:
            pass


# -------------------------
# Build App
# -------------------------
def build_application() -> Application:
    application = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("trending", trending_command))
    application.add_handler(CommandHandler("search", search_command))
    application.add_handler(CommandHandler("token", token_command))

    application.add_error_handler(error_handler)

    return application


# -------------------------
# Run Bot (FIXED)
# -------------------------
async def run_bot():
    application = build_application()

    logger.info("Starting bot...")

    await application.initialize()
    await application.start()

    await application.updater.start_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
    )

    try:
        while True:
            await asyncio.sleep(3600)
    finally:
        logger.info("Stopping bot...")

        await application.updater.stop()
        await application.stop()
        await application.shutdown()


# -------------------------
# Main Entry
# -------------------------
def main():
    try:
        asyncio.run(run_bot())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped.")
    except Exception:
        logger.exception("Fatal error")


if __name__ == "__main__":
    main()
