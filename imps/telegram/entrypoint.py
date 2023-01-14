from config import get_config
from imps.telegram.routers.chat import chat_router

from aiogram import Bot, Dispatcher

config = get_config()

def create_telegram_app() -> Dispatcher:

    bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
    app = Dispatcher(name=config.TELEGRAM_BOT_NAME)

    #routers registration
    app.include_router(chat_router)

    return app.run_polling(bot)
