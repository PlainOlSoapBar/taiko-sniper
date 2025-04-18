# Run this file to reset the database.

import asyncio
import os
from config import DB_NAME
from db.database import setup_database

DB_PATH = os.path.join("db", DB_NAME)

if os.path.exists(DB_NAME):
    os.remove(DB_NAME)
    print("✅ Database file deleted.")
else:
    print("⚠️ Database file not found.")



async def reset():
    await setup_database()
    print("✅ Database reinitialized.")


asyncio.run(reset())
