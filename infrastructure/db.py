from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Request
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    MONGO_URL = os.getenv("MONGO_URL")
    if not MONGO_URL:
        raise ValueError("MONGO_URL no está definido")
    return AsyncIOMotorClient(MONGO_URL)

client = get_client()
db = client["db_app_movil"]

async def get_db(request: Request):
    return db