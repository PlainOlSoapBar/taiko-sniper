import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")
COMMAND_PREFIX = os.getenv("COMMAND_PREFIX")
DB_NAME = os.getenv("DB_NAME")
DEVELOPER_MODE = os.getenv("DEVELOPER_MODE")