from keep_alive import keep_alive
from bot import bot
from db.database import setup_database
import asyncio
from config import TOKEN

async def load_extensions():
    await bot.load_extension("cogs.snipe")


async def main():
    await setup_database()
    await load_extensions()
    await bot.start(TOKEN)


if __name__ == "__main__":
    keep_alive()
    asyncio.run(main())
