from config import get_config
from time import sleep

import openai

config = get_config()

openai.api_key = config.OPENAI_API_KEY


async def chat(text: str) -> str:
    response = await openai.Completion.acreate(
        model=config.REQUEST_MODEL,
        prompt=text,
        temperature=config.REQUEST_TEMPERATURE,
        max_tokens=4000,
    )

    response_text = response.get("choices")[0].get("text")

    return response_text
