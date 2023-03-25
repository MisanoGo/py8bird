import logging
import asyncio
from enum import Enum

from tweepy import API, OAuth2BearerHandler

from aiogram import (Bot, Dispatcher, Router, F)
from aiogram.utils.keyboard import InlineKeyboardBuilder, CallbackData

from utils import env_conf



BOT_TOKEN: str = env_conf["BOT_TOKEN"]
OWNER_ID: str = env_conf["OWNER_ID"]
CHANNEL_ID: str = env_conf["CHANNEL_ID"]
TWITTER_TOKEN: str = env_conf["TWITTER_TOKEN"]

aiobot: Bot = Bot(BOT_TOKEN, parse_mode="HTML")
router: Router = Router()

auth = OAuth2BearerHandler(TWITTER_TOKEN)
api: API = API(auth)


class Action(str, Enum):
    send: str = "send"
    cancel: str = "cancel"

class AdminAction(CallbackData, prefix="adm"):
    action: Action
    twitte: str

async def getAdminApproval(tweet):
    msg: str = f"{tweet.text}"
    b: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for a in Action:
        b.button(
            text = a.value.title(),
            callback_data=AdminAction(action=a,twitte=tweet.id)
        )
    await aiobot.send_message(OWNER_ID,msg,reply_markup=b.as_markup())

@router.callback_query(AdminAction.filter(F.action == Action.send))
async def sendTwitte(callback_query,callback_data:AdminAction, bot: Bot):
    msg = api.get_status(callback_data.twitte).text
    sign: str = "\n ::"
    await bot.send_message(CHANNEL_ID,msg + sign)


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(aiobot)

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)

    m = main()
    asyncio.run(m)
