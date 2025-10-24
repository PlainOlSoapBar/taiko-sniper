import discord
from discord.ext import commands
from config import GUILD_ID, COMMAND_PREFIX, MODE

if (MODE == 'DEV'):
    from utils.logger import setup_logger
    setup_logger()

class TaikoSniper(commands.Bot):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} commands to Discord")
            await self.change_presence(
                activity=discord.Game(f"▄︻デ══━一 {self.command_prefix}snipe"),
            )

        except Exception as e:
            print(f"Error syncing commands: {e}")

intents = discord.Intents.default()
intents.message_content = True

bot = TaikoSniper(command_prefix=COMMAND_PREFIX, intents=intents)
