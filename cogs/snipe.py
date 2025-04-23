import discord
from discord import app_commands
from discord.ext import commands
from config import GUILD_ID
from db.database import get_db
from typing import Optional


class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="snipe",
        description="Snipe a member!",
    )
    @app_commands.describe(
        user="The user you are sniping.", image="Proof of your snipe."
    )
    async def snipe(
        self,
        interaction: discord.Interaction,
        user: discord.User,
        image: discord.Attachment,
    ):
        # Increase user's snipes count by 1
        db = await get_db()
        await db.execute(
            """
            INSERT INTO user_data (user_id, snipes)
            VALUES (?, 1)
            ON CONFLICT(user_id) DO UPDATE SET snipes = snipes + 1
        """,
            (interaction.user.id,),
        )
        await db.commit()

        # Increase receiver's sniped count by 1
        db = await get_db()
        await db.execute(
            """
            INSERT INTO user_data (user_id, sniped)
            VALUES (?, 1)
            ON CONFLICT(user_id) DO UPDATE SET sniped = sniped + 1
        """,
            (user.id,),
        )
        await db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.display_name} ▄︻デ══━一 {user.display_name}!",
            color=discord.Color.red(),
        )
        embed.set_image(url=image.url)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="stats",
        description="See statistics of yourself or another member.",
    )
    @app_commands.describe(
        user="The user whose stats you want to display. Leave empty to see your own stats."
    )
    async def stats(
        self, interaction: discord.Interaction, user: Optional[discord.User] = None
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
            embed = discord.Embed(
                title=f"📊 Stats for {target_user.display_name} 📊",
                description=f"📸 Snipes: `{snipes}`\n⚰️ Sniped: `{sniped}`",
                color=discord.Color.blue(),
            )
        else:
            embed = discord.Embed(
                title=f"No data found for {target_user.display_name}.",
                description="This user hasn't sniped or hasn't been sniped... yet.",
                color=discord.Color.dark_gray(),
            )

        embed.set_image(url=target_user.display_avatar.url)

        await interaction.response.send_message(embed=embed)

    # Admin only commands
    @app_commands.command(
        name="unsnipe",
        description="Made a mistake? Unsnipe a member. Admin priviledges required.",
    )
    @app_commands.describe(
        user="The user you are unsniping."
    )
    async def unsnipe(
        self,
        interaction: discord.Interaction,
        user: discord.User,
    ):
        # Check if the user has admin
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "You do not have permission to use this command.", ephemeral=True
            )
            return
        
        # Decrease user's snipes count by 1
        db = await get_db()
        await db.execute(
            """
            INSERT INTO user_data (user_id, snipes)
            VALUES (?, 1)
            ON CONFLICT(user_id) DO UPDATE SET snipes = snipes - 1
        """,
            (interaction.user.id,),
        )
        await db.commit()

        # Decrease receiver's sniped count by 1
        db = await get_db()
        await db.execute(
            """
            INSERT INTO user_data (user_id, sniped)
            VALUES (?, 1)
            ON CONFLICT(user_id) DO UPDATE SET sniped = sniped - 1
        """,
            (user.id,),
        )
        await db.commit()

        embed = discord.Embed(
            title=f"{user.display_name} has been unsniped.",
            color=discord.Color.red(),
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    async def cog_load(self):
        guild = discord.Object(id=GUILD_ID)
        self.bot.tree.add_command(self.snipe, guild=guild)
        self.bot.tree.add_command(self.stats, guild=guild)
        self.bot.tree.add_command(self.unsnipe, guild=guild)

async def setup(bot):
    await bot.add_cog(Snipe(bot))
