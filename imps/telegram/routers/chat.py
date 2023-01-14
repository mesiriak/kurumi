from aiogram import Router, types
from aiogram.methods.send_message import SendMessage

from core.openai_api.openai_entrypoint import chat

chat_router = Router()


@chat_router.message()
async def send_welcome(message: types.Message):

    response = await chat(message.text)

    return SendMessage(chat_id=message.chat.id, text=response)