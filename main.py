from imps.telegram.entrypoint import create_telegram_app

import asyncio


async def main():
    telegram_app = asyncio.create_task(
        create_telegram_app()
    )

    # add apps inside gather
    await asyncio.gather(telegram_app) 

if __name__ == '__main__':
    asyncio.run(main())
