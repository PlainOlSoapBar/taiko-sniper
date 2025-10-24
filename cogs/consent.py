import discord
from discord import app_commands
from discord.ext import commands
from config import GUILD_ID
from db.database import get_db
from typing import Optional


class Consent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ============================
    # Consent Command
    # ============================
    @app_commands.command(
        name="consent",
        description="**REQUIRED** Give consent to Don-chan.",
    )
    async def consent(
        self,
        interaction: discord.Interaction,
    ):
        db = await get_db()
        async with db.execute(
            "SELECT consent FROM user_data WHERE user_id = ?",
            (interaction.user.id,),
        ) as cursor:
            consent = await cursor.fetchone()
        
        if (consent == 1): 
            embed = discord.Embed(
                title="You have already given consent!",
                description="Use /unconsent if you wish to revoke your consent!",
                color=discord.Color.red(),
            )
        else:
            # Change consent value to 1
            db = await get_db()
            await db.execute(
                """
                INSERT INTO user_data (user_id, consent)
                VALUES (?, 1)
                ON CONFLICT(user_id) DO UPDATE SET consent=1
                """,
                (interaction.user.id,),
            )
            await db.commit()

            embed = discord.Embed(
                title="Consent given!",
                description="Use /unconsent if you wish to revoke your consent!",
                color=discord.Color.blue(),
            )

        await interaction.response.send_message(embed=embed, ephemeral=True)

    # ============================
    # Unconsent Command
    # ============================
    @app_commands.command(
        name="unconsent",
        description="Revoke consent from Don-chan.",
    )
    async def unconsent(
        self,
        interaction: discord.Interaction,
    ):
        db = await get_db()
        async with db.execute(
            "SELECT consent FROM user_data WHERE user_id = ?",
            (interaction.user.id,),
        ) as cursor:
            consent = await cursor.fetchone()
        
        if (consent == 0): 
            embed = discord.Embed(
                title="You have not given consennt to Don-chan!",
                description="No further action is necessary.",
                color=discord.Color.red(),
            )
        else:
            # Change consent value to 0
            db = await get_db()
            await db.execute(
                """
                INSERT INTO user_data (user_id, consent)
                VALUES (?, 0)
                ON CONFLICT(user_id) DO UPDATE SET consent=0
                """,
                (interaction.user.id,),
            )
            await db.commit()

            embed = discord.Embed(
                title="Consent revoked!",
                description="Use /consent if you wish to give your consent again!",
                color=discord.Color.blue(),
            )

        await interaction.response.send_message(embed=embed, ephemeral=True)

    async def cog_load(self):
        guild = discord.Object(id=GUILD_ID)
        self.bot.tree.add_command(self.consent, guild=guild)
        self.bot.tree.add_command(self.unconsent, guild=guild)

async def setup(bot):
    await bot.add_cog(Consent(bot))
