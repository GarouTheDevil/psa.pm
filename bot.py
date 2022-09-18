import base64
import re
import time
import requests
from bs4 import BeautifulSoup

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import aiohttp
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from pyrogram.errors import UserNotParticipant, UserBannedInChannel 

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
CRYPT = 'ajRmMzd2ZEdxL055ZC9vMHlwNGZwZUE4Zm9MSzFUVDRETU9ESm4xU1lqcz0%3D'
#API_KEY = environ.get('API_KEY')

bot = Client('LinkByPass bot',
             api_id= "1543212",
             api_hash= "d47de4b25ddf79a08127b433de32dc84",
             bot_token= "5462389029:AAEtTZT0mopLzVGM45SUmKHIFto_nEjc48M")


@bot.on_message(filters.command('start'))
async def start(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("You are Banned")
        return
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("**Your Banned**")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**Join Update Channel**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await update.reply_text(Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("HELP", callback_data = "ghelp"),
                        InlineKeyboardButton("ABOUT", callback_data = "about"),
                        InlineKeyboardButton("CLOSE", callback_data = "close")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
            )

@bot.on_message(filters.command('help'))
async def help(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("You are Banned")
        return
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("**Your Banned**")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**Join Update Channel**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await update.reply_text(Translation.HELP_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('ABOUT', callback_data = "about"),
                    InlineKeyboardButton('CLOSE', callback_data = "close")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
            )

@bot.on_message(filters.command('about'))
async def about(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("You are Banned")
        return
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("**Your Banned**")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**Join Update Channel**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await update.reply_text(
        text= Translation.ABOUT_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('HELP', callback_data = "ghelp"),
                    InlineKeyboardButton('CLOSE', callback_data = "close")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
            )

url = input("Enter the Url : ")

client = requests.Session()
h = {
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}
res = client.get(url, cookies={}, headers=h)

url = 'https://try2link.com/'+re.findall('try2link\.com\/(.*?) ', res.text)[0]

res = client.head(url)

id = re.findall('d=(.*?)&', res.headers['location'])[0]
id = base64.b64decode(id).decode('utf-8')

url += f'/?d={id}'
res = client.get(url)

bs4 = BeautifulSoup(res.content, 'html.parser')
inputs = bs4.find_all('input')
data = { input.get('name'): input.get('value') for input in inputs }

time.sleep(6.5)
res = client.post(
    'https://try2link.com/links/go',
    headers={
        'referer': url,
        'x-requested-with': 'XMLHttpRequest',
    }, data=data
)
out = res.json()['url'].replace('\/','/')

print(out)
