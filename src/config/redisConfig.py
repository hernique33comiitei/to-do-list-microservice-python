import os
import aioredis
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")

async def redis_connection():
    return await aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")
