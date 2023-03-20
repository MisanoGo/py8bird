import tweepy
from aiogram import Bot


BOT_TOKEN: str = ""
CHANNEL_ID: int = 0

TWITTER_TOKEN: str = ""

class TwittePublisher(tweepy.StreamingClient):
    aiobot: Bot = Bot(BOT_TOKEN)

    def on_tweet(self, tweet):
        if self.check(tweet):
            self.retwitte(tweet)
            self.publish(tweet)

    def check(self,tweet) -> bool: # TODO
        return True

    def retwitte(self, tweet):
        pass

    #def adminApproval(self, tweet) -> :
        #pass

    def publish(self,tweet):
        msg: str = f"{tweet.text}\n"
        self.aiobot.send_message(CHANNEL_ID,msg)



printer = TwittePublisher(TWITTER_TOKEN)
printer.sample()
