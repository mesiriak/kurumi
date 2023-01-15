from aiogram import Router
from aiogram.types import Message, BotCommand
from aiogram.methods.send_message import SendMessage

from core.openai_api.entrypoint import chat

chat_router = Router()


@chat_router.message()
async def openai_chat(message: Message) -> SendMessage:

    response = await chat(message.text)

    return SendMessage(chat_id=message.chat.id, text=response)
