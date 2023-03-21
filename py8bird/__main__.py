from typing import List

import tweepy

from main import TwittePublisher
import utils

def main():
    TWITTER_TOKEN: str = utils.env_conf["TWITTER_TOKEN"]

    key_filter: List[str] = [
        "python",
    ]
 
    tp = TwittePublisher(TWITTER_TOKEN)

    tp.add_rules([tweepy.StreamRule(i) for i in key_filter])
    tp.filter()

if __name__=="__main__":
    main()
