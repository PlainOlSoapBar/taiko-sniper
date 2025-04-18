import aiosqlite
from config import DB_NAME
import os

DB_PATH = os.path.join(os.path.dirname(__file__), DB_NAME)


async def get_db():
    return await aiosqlite.connect(DB_PATH)


async def setup_database():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data (
                user_id INTEGER PRIMARY KEY,
                snipes INTEGER DEFAULT 0,
                sniped INTEGER DEFAULT 0
            )
            """
        )
        await db.commit()
