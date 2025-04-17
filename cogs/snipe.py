import discord
from discord import app_commands
from discord.ext import commands
from config import GUILD_ID


class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="snipe",
        description="Snipe a member!",
    )
    async def snipe(
        self,
        interaction: discord.Interaction,
        user: discord.User,
        image: discord.Attachment,
    ):
        embed = discord.Embed(
            title=f"{interaction.user.display_name} sniped {user.display_name}!"
        )
        embed.set_image(url=image.url)
        await interaction.response.send_message(embed=embed)

    async def cog_load(self):
        guild = discord.Object(id=GUILD_ID)
        self.bot.tree.add_command(self.snipe, guild=guild)


async def setup(bot):
    await bot.add_cog(Snipe(bot))
