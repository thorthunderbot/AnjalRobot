import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION")
BOT_USERNAME = getenv("BOT_USERNAME")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1420377975").split()))
NETWORK = getenv("NETWORK")
GROUP = getenv("GROUP")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/18b5cd1061adfe09f7459.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/18b5cd1061adfe09f7459.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/18b5cd1061adfe09f7459.jpg")
aiohttpsession = aiohttp.ClientSession()

