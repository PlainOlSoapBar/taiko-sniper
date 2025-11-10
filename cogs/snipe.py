import discord
from discord import app_commands
from discord.ext import commands
from config import GUILD_ID
from db.database import get_db

# Check if the user has admin
# if not interaction.user.guild_permissions.administrator:
#     await interaction.response.send_message(
#         "You do not have permission to use this command.", ephemeral=True
#     )
#     return


class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ============================
    # Snipe Command
    # ============================
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
        # Prevent sniping yourself or bots
        if interaction.user.id == user.id:
            embed = discord.Embed(
                title="Invalid snipe!",
                description="You can't snipe yourself, silly!",
                color=discord.Color.red(),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        if user.bot:
            embed = discord.Embed(
                title="Invalid snipe!",
                description="You can't snipe non-humans, silly!",
                color=discord.Color.red(),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        # Prevent sniping if either members have not given consent
        # This is not necessary for /unsnipe imo
        db = await get_db()
        async with db.execute(
            "SELECT consent FROM user_data WHERE user_id = ?",
            (interaction.user.id,),
        ) as cursor:
            sniper_consent_row = await cursor.fetchone()
        sniper_consent = sniper_consent_row[0] if sniper_consent_row else 0

        if sniper_consent == 0:
            embed = discord.Embed(
                title="Invalid snipe!",
                description="You cannot snipe without giving consent with `/consent`.",
                color=discord.Color.red(),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        db = await get_db()
        async with db.execute(
            "SELECT consent FROM user_data WHERE user_id = ?",
            (user.id,),
        ) as cursor:
            target_consent_row = await cursor.fetchone()
        target_consent = target_consent_row[0] if target_consent_row else 0

        if target_consent == 0:
            embed = discord.Embed(
                title="Invalid snipe!",
                description="The member you are trying to snipe has not given consent with `/consent`.",
                color=discord.Color.red(),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        # Check if image size is within acceptable limits (10 MB)
        if (image.size / 1024 / 1024) > 10:
            embed = discord.Embed(
                title="Invalid snipe!",
                description="The image file size is too high! Max is 10MB.",
                color=discord.Color.red(),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

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

        # Retrieve snipes for the command user
        db = await get_db()
        async with db.execute(
            "SELECT snipes FROM user_data WHERE user_id = ?",
            (interaction.user.id,),
        ) as cursor:
            snipes_row = await cursor.fetchone()
        snipes = snipes_row[0] if snipes_row else 0

        # Retrieve sniped for the target user
        async with db.execute(
            "SELECT sniped FROM user_data WHERE user_id = ?",
            (user.id,),
        ) as cursor:
            sniped_row = await cursor.fetchone()
        sniped = sniped_row[0] if sniped_row else 0

        # Send message
        embed = discord.Embed(
            title=f"{interaction.user.display_name} ▄︻デ══━一 {user.display_name}",
            description=f"{interaction.user.mention} now has {snipes} snipes!\n{user.mention} has been sniped {sniped} time(s)!",
            color=discord.Color.red(),
        )
        await interaction.response.send_message(
            content=None, file=await image.to_file()
        )
        await interaction.followup.send(embed=embed)

    # ============================
    # Unsnipe Command
    # ============================
    @app_commands.command(
        name="unsnipe",
        description="Made a mistake? Unsnipe a member.",
    )
    @app_commands.describe(user="The member you are unsniping.")
    async def unsnipe(
        self,
        interaction: discord.Interaction,
        user: discord.User,
    ):
        # Prevent unsniping yourself or bots
        if interaction.user.id == user.id:
            embed = discord.Embed(
                title="Invalid unsnipe!",
                description="You can't unsnipe yourself, silly!",
                color=discord.Color.red(),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        if user.bot:
            embed = discord.Embed(
                title="Invalid unsnipe!",
                description="You can't unsnipe non-humans, silly!",
                color=discord.Color.red(),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        # Prevent unsniping someone with zero snipeds
        db = await get_db()
        async with db.execute(
            "SELECT sniped FROM user_data WHERE user_id = ?",
            (user.id,),
        ) as cursor:
            sniped_row = await cursor.fetchone()
            sniped = sniped_row[0] if sniped_row else 0

        if sniped == 0:
            embed = discord.Embed(
                title="Invalid unsnipe!",
                description="You can't unsnipe a member with zero snipeds!",
                color=discord.Color.red(),
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        # Decrease user's snipes count by 1
        db = await get_db()
        await db.execute(
            """
            INSERT INTO user_data (user_id, snipes)
            VALUES (?, 1)
            ON CONFLICT(user_id) DO UPDATE SET snipes = MAX(snipes - 1, 0)
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
            ON CONFLICT(user_id) DO UPDATE SET sniped = MAX(sniped - 1, 0)
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
        self.bot.tree.add_command(self.unsnipe, guild=guild)


async def setup(bot):
    await bot.add_cog(Snipe(bot))
