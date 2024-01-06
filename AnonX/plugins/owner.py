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
        photo=f"https://telegra.ph/file/7f0490e53d3cce83504af.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                    text="ᴏᴡɴᴇʀ",
                    callback_data="help_callback hb1",
                    )
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
        photo=f"https://telegra.ph/file/7f0490e53d3cce83504af.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                    text="ᴏᴡɴᴇʀ",
                    callback_data="help_callback hb1",
                    )
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
        photo=f"https://telegra.ph/file/7f0490e53d3cce83504af.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ɢᴇᴛ ꜱᴜᴘᴘᴏʀᴛ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ꜱᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP)
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
        photo=f"https://telegra.ph/file/7f0490e53d3cce83504af.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ɢᴇᴛ ꜱᴜᴘᴘᴏʀᴛ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ꜱᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP)
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
        photo=f"https://telegra.ph/file/7f0490e53d3cce83504af.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ɢᴇᴛ ꜱᴜᴘᴘᴏʀᴛ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ꜱᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP)
                ]
            ]
        ),
    )

