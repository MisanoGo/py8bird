from typing import List
from enum import Enum
import asyncio

from tweepy import StreamingClient, API,OAuth2BearerHandler, StreamRule
from tweepy.models import Status
from aiogram import Bot, Dispatcher, Router, F

from aiogram.utils.keyboard import CallbackData, InlineKeyboardBuilder as IKB

from utils import env_conf


BOT_TOKEN: str = env_conf["BOT_TOKEN"]
CHANNEL_ID: str = env_conf["CHANNEL_ID"]
TWITTER_TOKEN: str = env_conf["TWITTER_TOKEN"]

aiobot: Bot = Bot(BOT_TOKEN)
router: Router = Router()

auth = OAuth2BearerHandler(TWITTER_TOKEN)
api: API = API(auth)


class Action(str, Enum):  
    cancel: str = "cancel"
    send: str = "send"

class AdminAction(CallbackData, prefix="adm"):
    action: Action
    tweet_id: str

async def getAdminApproval(tweet):
    b = IKB()
    for a in Action:
        b.button(text=a.value.title(),callback_data=AdminAction(action=a,tweet_id=tweet.id))
    msg: str = f"{tweet.text}\n"
    await aiobot.send_message(CHANNEL_ID,msg,reply_markup=b.as_markup())

class TwittePublisher(StreamingClient):
    def on_tweet(self, tweet):

        asyncio.run(getAdminApproval(tweet))
  

@router.callback_query(AdminAction.filter(F.action == Action.send))
async def publishTwitte(callback_query,callback_data: AdminAction, bot: Bot):
    api.retweet(callback_data.tweet_id)

    tweet = api.get_status(callback_data.tweet_id)
    bot.send_message(CHANNEL_ID,tweet)

def main():
    key_filter: List[str] = [
        "python",
    ]
    dp = Dispatcher()
    dp.include_router(router)

    tp = TwittePublisher(TWITTER_TOKEN)
    tp.add_rules([StreamRule(i) for i in key_filter])
    tp.filter()

    asyncio.run(dp.start_polling(aiobot))



if __name__=="__main__":
    main()

