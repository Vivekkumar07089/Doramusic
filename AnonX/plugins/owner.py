from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AnonX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/8998ddca2f42a4fac4efd.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴠɪᴠᴇᴋ", url=f"https://t.me/vivekkumar0708")
                ]
            ]
        ),
    )
@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/8998ddca2f42a4fac4efd.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴠɪᴠᴇᴋ", url=f"https://t.me/vivekkumar0708")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("support")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/987c3d0db44f6dd58fb2e.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ sᴜᴘᴘᴏʀᴛ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/bseb9th")
                ]
            ]
        ),
    )
@app.on_message(
    filters.command("support")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/987c3d0db44f6dd58fb2e.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ sᴜᴘᴘᴏʀᴛ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/bseb9th")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("support")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/987c3d0db44f6dd58fb2e.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ sᴜᴘᴘᴏʀᴛ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/bseb9th")
                ]
            ]
        ),
    )
