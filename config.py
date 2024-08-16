import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "6534707"))
API_HASH = environ.get("API_HASH", "4bcc61d959a9f403b2f20149cbbe627a")
BOT_TOKEN = environ.get("BOT_TOKEN", "7509328585:AAFpxHizMnpeY6I9O6QvAljmG7lIGvgCc9Y")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002244364312"))
ADMINS = int(environ.get("ADMINS", "1430593323"))
DB_URI = environ.get("DB_URI", "mongodb+srv://nhere118:jSsmgEs1uEqnlbrZ@cluster0.rdkih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
