import discord
from discord.ext import commands
from config import TOKEN, GUILD_ID
from utils.logger import setup_logger

setup_logger()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await bot.tree.sync(guild=guild)
        print(f"Synced {len(synced)} commands to Guild {guild.id}")

    except Exception as e:
        print(f"Error syncing commands: {e}")


async def load_extensions():
    await bot.load_extension("cogs.snipe")


import asyncio


async def main():
    await load_extensions()
    await bot.start(TOKEN)


asyncio.run(main())
