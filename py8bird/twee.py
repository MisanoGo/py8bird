import asyncio
import logging

from tweepy.asynchronous.streaming import  AsyncStreamingClient, StreamRule

from aiobot import getAdminApproval
from utils import env_conf, key_filters


TWITTER_TOKEN: str = env_conf["TWITTER_TOKEN"]


srl = [StreamRule(i) for i in key_filters()]

class TwittePublisher(AsyncStreamingClient):
    async def on_tweet(self, tweet):
        await getAdminApproval(tweet)

async def main():
    logging.basicConfig(level=logging.DEBUG)
    tpc: AsyncStreamingClient = TwittePublisher(TWITTER_TOKEN)
    await tpc.add_rules(srl)
    await tpc.filter()


if __name__=="__main__":
    m = main()
    asyncio.run(m)
