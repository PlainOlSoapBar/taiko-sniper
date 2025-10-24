import discord
from discord import app_commands
from discord.ext import commands
from config import GUILD_ID
from db.database import get_db
from typing import Optional

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ============================
    # Stats Command
    # ============================
    @app_commands.command(
        name="stats",
        description="See statistics of yourself or another member.",
    )
    @app_commands.describe(
        user="The user whose stats you want to display. Leave empty to see your own stats.", private="Privately display stats. Default: True"
    )
    async def stats(
        self,
        interaction: discord.Interaction,
        user: Optional[discord.User] = None,
        private: Optional[bool] = True,
    ):
        target_user = user or interaction.user

        db = await get_db()
        async with db.execute(
            "SELECT snipes, sniped FROM user_data WHERE user_id = ?",
            (target_user.id,),
        ) as cursor:
            row = await cursor.fetchone()

        if row:
            snipes, sniped = row
            kd = snipes / sniped if sniped > 0 else float('inf')
            embed = discord.Embed(
                title=f"📊 Stats for {target_user.display_name} 📊",
                description=f"📸 Snipes: `{snipes}`\n⚰️ Sniped: `{sniped}`\n🎯 K/D: `{kd:.2f}`",
                color=discord.Color.blue(),
            )
        else:
            embed = discord.Embed(
                title=f"No data found for {target_user.display_name}.",
                description="This user hasn't sniped or hasn't been sniped... yet.",
                color=discord.Color.dark_gray(),
            )

        if not private:
            await interaction.response.send_message(embed=embed)
            return

        await interaction.response.send_message(embed=embed, ephemeral=True)

    async def cog_load(self):
        guild = discord.Object(id=GUILD_ID)
        self.bot.tree.add_command(self.stats, guild=guild)

async def setup(bot):
    await bot.add_cog(Stats(bot))
