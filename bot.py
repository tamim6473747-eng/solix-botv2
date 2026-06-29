import logging
import asyncio

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
)

from config import BOT_TOKEN

from handlers.start import start_command
from handlers.help import help_command
from handlers.trending import trending_command
from handlers.search import search_command
from handlers.token import token_command

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("Solix")


def build_app():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("trending", trending_command))
    app.add_handler(CommandHandler("search", search_command))
    app.add_handler(CommandHandler("token", token_command))

    return app


async def run():
    app = build_app()

    await app.initialize()
    await app.start()

    logger.info("🚀 Bot running stable...")

    # 🔥 KEEP PROCESS ALIVE (IMPORTANT FOR RENDER)
    await asyncio.Event().wait()


def main():
    asyncio.run(run())


if __name__ == "__main__":
    main()
