import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (    ("Minggu", 60 * 60 * 24 * 7),    ("Hari", 60 * 60 * 24),    ("Jam", 60 * 60),    ("Menit", 60),    ("Detik", 1),)
async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["تحديث"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("①")
    await loli.edit("②")
    await loli.edit("③")
    await loli.edit("④")
    await loli.edit("⑤")
    await loli.edit("⑥")
    await loli.edit("⑦")
    await loli.edit("⑧")
    await loli.edit("⑨")
    await loli.edit("✅𝙏𝙊𝙋𝘼𝘾:@OYOYV تم اعاده تشغيل سورس ميوزك توب")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.command(["اوامري"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    photo="https://telegra.ph/file/40c0ab31719a780e37b5c.jpg"
    TOPAC = f"""
<b> هلاا عمري 🤎🎹 {m.from_user.mention}!


——————×—————

↲🎷 | لتشغيل صوتية في المكالمة أرسل ⇦ [ {HNDLR}تشغيل  + اسم الاغنية ]
↲🎹 | لتشغيل فيديو في المكالمة  ⇦ [ {HNDLR}تشغيل_فيديو  + اسم الاغنية ]
———————×———————

↲🎷 | لأيقاف الاغنية او الفيديو مؤقتآ  ⇦ [ {HNDLR}استئناف ] 
↲🎹 | لأعاده تشغيل الاغنية ⇦  [ {HNDLR}ايقاف_الاستئناف ]
↲🎷 | لأيقاف الاغنية  ⇦ [ {HNDLR}ايقاف ] 
↲🎹 | لتغطي الاغنية الحالية و تشغيل الاغنية التالية ⇦ [ {HNDLR}التالي ]
↲🥁 | لتشغيل الاغنية عشوائية من قناة او مجموعة  ⇦ [ {HNDLR}اغنيه عشوائية ]
———————×———————

↲🎷 | لتحميل صوتية أرسل ⇦ [ {HNDLR}تحميل + اسم الاغنية او الرابط ]
↲🎹 | لتحميل فيديو  ⇦  [ {HNDLR}تحميل_فيديو + اسم الاغنية او الرابط ]


↲🎷 | حول السورس ⇦  [ {HNDLR}السورس ]
↲🎹 | لأعاده تشغيل التنصيب أرسل ⇦  [ {HNDLR}تحديث ]
———————×———————
المطور 🇮🇶 : @GTT_G 
القناة 🇮🇶 :  @OYOYV"""
    await m.reply(TOPAC)
@Client.on_message(filters.command(["معلومات"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋  اهلا {m.from_user.mention}!

🎶 هذا هو سورس ميوزك توب 
🤖 اختصاص هذا البوت تنزيل المقاطع الصوتيه
 وتشغيل او تنزيل مقاطع الفيديو و تشغيل 
وتشغيل الاغاني ول فيديوهات في المكالمات

"""
    await m.reply(REPO, disable_web_page_preview=True)
