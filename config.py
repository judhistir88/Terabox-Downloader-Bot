from os import environ

# BOT CONFIG
API_ID = environ.get("API_ID", "")  # api id
API_HASH = environ.get("API_HASH", "")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "")  # bot token

# ATLAS
ATLAS_URI = environ.get("ATLAS_URI", "")  # Atlas connection URI

ADMINS = [environ.get("ADMINS", "")]  # List of admin IDs
OWNER_ID = environ.get("OWNER_ID", "")  # Owner ID
PRIVATE_CHAT_ID = environ.get("PRIVATE_CHAT_ID", "")  # Private chat ID
USER_CHANNEL = environ.get("USER_CHANNEL", "")  # User channel ID
DUMP_CHANNEL = environ.get("DUMP_CHANNEL", "")  # Dump channel ID

# Config
COOKIE = environ.get("COOKIE", "")
