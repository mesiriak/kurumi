import discord

from config import get_config

config = get_config()


async def create_discord_app() -> None:
    intents = discord.Intents.default()
    intents.message_content = True

    bot = discord.Client(intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')

    await bot.start(config.DISCORD_BOT_TOKEN)
