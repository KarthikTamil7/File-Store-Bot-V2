#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🤖 My Name : <a href='https://t.me/HMTD_File_Store_V2_Bot'>HMTD File Store V2 Bot</a>\n🧑🏻‍💻 Developer : <a href='https://hmtd-movies.blogspot.com/'>Karthik</a>\n📝 Language : <a href='https://www.python.org/'>Python3</a>\n📚 Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\nℹ️ Source Code : <a href='http://bit.ly/3IJdZFA'>Click here</a>\n📡 Hosted on : <a href='https://heroku.com/'>Heroku</a>\n🌐 Website : <a href='https://hmtd-movies.blogspot.com/'>HMTD Movies</a>\n🧑🏻‍ Feedback : <a href='https://t.me/HMTD_Feedback_Bot'>HMTD Feedback Bot</a>\n📢 Updates Channel : <a href='https://t.me/HMTD_Links'>HMTD Links</a>\n👥 Discussion Group : <a href='https://t.me/HMTD_Discussion_Group'>Discussion Group</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
