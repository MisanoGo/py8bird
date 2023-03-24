import asyncio
import logging

from tweepy.asynchronous.streaming import  AsyncStreamingClient, StreamRule
from aiogram import Bot

from utils import env_conf, key_filters


BOT_TOKEN: str = env_conf["BOT_TOKEN"]
OWNER_ID: str = env_conf["OWNER_ID"]
TWITTER_TOKEN: str = env_conf["TWITTER_TOKEN"]

aiobot: Bot = Bot(BOT_TOKEN, parse_mode="HTML")
srl = [StreamRule(i) for i in key_filters()]

async def sendTwitte(tweet):
    await aiobot.send_message(OWNER_ID,tweet.text)

class TwittePublisher(AsyncStreamingClient):
    async def on_tweet(self, tweet):
        await sendTwitte(tweet)

async def main():
    tpc: AsyncStreamingClient = TwittePublisher(TWITTER_TOKEN)
    #await tpc.delete_rules()
    await tpc.add_rules(srl)
    await tpc.filter()


if __name__=="__main__":
    logging.basicConfig(filename='.log',level=logging.DEBUG)
    m = main()
    asyncio.run(m)
