import discord
from discord import app_commands
from discord.ext import commands
from config import GUILD_ID
from db.database import get_db
from typing import Optional


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ============================
    # Help Command
    # ============================
    @app_commands.command(
        name="help",
        description="See list of available commands.",
    )
    async def help(
        self,
        interaction: discord.Interaction,
    ):
        commands_list = self.bot.tree.get_commands()

        embed = discord.Embed(
            title="Available Commands",
            color=discord.Color.dark_gray(),
        )

        if commands_list:
            for cmd in commands_list:
                if cmd != self.help:
                    embed.add_field(
                        name=f"/{cmd.name}",
                        value=cmd.description or "No description provided",
                        inline=False
                    )
        else:
            embed.description = "No commands available."

        await interaction.response.send_message(embed=embed, ephemeral=True)

    async def cog_load(self):
        guild = discord.Object(id=GUILD_ID)
        self.bot.tree.add_command(self.help, guild=guild)

async def setup(bot):
    await bot.add_cog(Help(bot))
