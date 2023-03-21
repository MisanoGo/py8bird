from typing import List
import asyncio

import tweepy
from aiogram import Bot

from utils import env_conf


BOT_TOKEN: str = env_conf["BOT_TOKEN"]
CHANNEL_ID: str = env_conf["CHANNEL_ID"]


class TwittePublisher(tweepy.StreamingClient):
    aiobot: Bot = Bot(BOT_TOKEN)

    def on_tweet(self, tweet):
        if self.check(tweet):
            self.retwitte(tweet)
            asyncio.run(self.publish(tweet))

    def check(self,tweet) -> bool: # TODO
        return True

    def retwitte(self, tweet):
        pass

    #def adminApproval(self, tweet) -> :
        #pass

    async def publish(self,tweet):
        msg: str = f"{tweet.text}\n"
        print(msg)
        await self.aiobot.send_message(CHANNEL_ID,msg)
