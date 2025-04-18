import discord
from discord.ext import commands
from utils.logger import setup_logger
import asyncio
from config import TOKEN, GUILD_ID, COMMAND_PREFIX


setup_logger()

class TaikoSniper(commands.Bot):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

        try:
            guild = discord.Object(id=GUILD_ID)
            synced = await self.tree.sync(guild=guild)
            await self.change_presence(
                activity=discord.Game(f"{self.command_prefix}snipe"),
            )
            print(f"Synced {len(synced)} commands to Guild {guild.id}")

        except Exception as e:
            print(f"Error syncing commands: {e}")

async def load_extensions():
    await bot.load_extension("cogs.snipe")

async def main():
    await load_extensions()
    await bot.start(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

bot = TaikoSniper(command_prefix=COMMAND_PREFIX, intents=intents)

if __name__ == "__main__":
    asyncio.run(main())
