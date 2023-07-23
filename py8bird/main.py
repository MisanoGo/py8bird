import asyncio

from tweepy import StreamingClient
from aiogram import Bot

from utils import env_conf, key_filters


BOT_TOKEN: str = env_conf["BOT_TOKEN"]
OWNER_ID: str = env_conf["OWNER_ID"]
TWITTER_TOKEN: str = env_conf["TWITTER_TOKEN"]

aiobot: Bot = Bot(BOT_TOKEN, parse_mode="HTML")

async def sendTwitte(tweet):
    await aiobot.send_message(OWNER_ID,tweet.text)

class TwittePublisher(StreamingClient):
    def on_tweet(self, tweet):
        asyncio.run(sendTwiite(tweet))
 

def main():
    tp = TwittePublisher(TWITTER_TOKEN)
    tp.add_rules([StreamRule(i) for i in key_filters])
    tp.filter()

if __name__=="__main__":
    main()
