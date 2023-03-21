from typing import List
import tweepy
from aiogram import Bot
import asyncio

BOT_TOKEN: str = "5996837717:AAEvTxi4RnvcL5rVx4pqdBcYByyQZhyjSXE"
CHANNEL_ID: str = "@msn_test_channel"
TWITTER_TOKEN: str = "AAAAAAAAAAAAAAAAAAAAALvucwEAAAAAXwswoYd3vRqXkeuXPlcLUmLDiTw%3D3UGMWfkOgQbSSRfbH19nX1Ai24GpUBhD9dCGBASgPszc2ium58"

key_filter: List[str] = [
    "python"
]

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



tp = TwittePublisher(TWITTER_TOKEN)

tp.add_rules([tweepy.StreamRule(i) for i in key_filter])
tp.filter()
#tp.sample()
