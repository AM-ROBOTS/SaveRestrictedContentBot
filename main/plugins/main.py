#Github.com/Vasusen-code

import time, os

from .. import bot as Drone
from .. import userbot, Bot
from .. import FORCESUB as fs
from main.plugins.pyroplug import get_msg

from telethon import events
from telethon.tl.types import DocumentAttributeVideo

from ethon.pyfunc import video_metadata
from ethon.telefunc import fast_upload, fast_download, force_sub

from main.plugins.helpers import get_link, join, screenshot

ft = f"To use this bot you've to join @{fs}."

# To-Do:
# Make these codes shorter and clean
# ofc will never do it. 

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    if event.is_reply:
        return
    try:
        link = get_link(event.text)
        if not link:
            return
    except TypeError:
        return
    s, r = await force_sub(event.client, fs, event.sender_id, ft)
    if s == True:
        await event.reply(r)
        return
    edit = await event.reply("Processing!")
    if 't.me/+' in link:
        q = await join(userbot, link)
        await edit.edit(q)
        return 
    if 't.me/' in link:
        await get_msg(userbot, Bot, event.sender_id, edit.id, link, 0)
        
