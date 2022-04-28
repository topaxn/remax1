import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# للنشر المحلي
if os.path.exists(".env"):
    load_dotenv(".env")
# الفارات
API_ID = int(os.getenv("ايبي ايدي"))
API_HASH = os.getenv("ايبي هاش")
SESSION = os.getenv("بايرو توب")
HNDLR = os.getenv("علامه او رمز", "$")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))
contact_filter = filters.create(    lambda _, __, message: (message.from_user and message.from_user.is_contact)    or message.outgoing)
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicTop"))
call_py = PyTgCalls(bot)
