from pydantic import BaseSettings
from functools import lru_cache


class Config(BaseSettings):
    OPENAI_API_KEY: str
    
    REQUEST_MODEL: str = "text-davinci-003"
    REQUEST_TEMPERATURE: float = 0.9 # default == 0.7

    TELEGRAM_BOT_NAME: str = "kurumi"
    TELEGRAM_BOT_TOKEN: str

    class Config:
        env_file = '.env'


@lru_cache()
def get_config() -> Config:
    config = Config()
    return config
