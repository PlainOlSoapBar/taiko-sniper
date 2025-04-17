import discord
from discord.ext import commands
from discord import app_commands

import os
from dotenv import load_dotenv

import logging
import logging.handlers

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
logging.getLogger("discord.http").setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename="discord.log",
    encoding="utf-8",
    maxBytes=32 * 1024 * 1024,  # 32 MB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(
    "[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{"
)
handler.setFormatter(formatter)
logger.addHandler(handler)

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="/", intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await client.tree.sync(guild=guild)
        print(f"Synced {len(synced)} commands to Guild {guild.id}")

    except Exception as e:
        print(f"Error syncing commands: {e}")


@client.tree.command(
    name="snipe", description="Snipe a member!", guild=discord.Object(id=GUILD_ID)
)
async def snipe(
    interaction: discord.Interaction, user: discord.User, image: discord.Attachment
):
    embed = discord.Embed(title=f"{interaction.user} sniped {user.display_name}!")

    embed.set_image(url=image.url)

    await interaction.response.send_message(embed=embed)


client.run(TOKEN, log_handler=None)
