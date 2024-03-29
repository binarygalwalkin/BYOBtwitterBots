# __author__ = "Sebastian Gumprich"
# __modified by__ = "binarygalwalkin"
# __credits__ = ["Sebastian Gumprich", "binarygalwalkin"]
# __license__ = "GPL"
# __version__ = "v2.0"
# __maintainer__ = "binarygalwalkin"



from twitter import Twitter, OAuth
from bs4 import BeautifulSoup
from urllib import request
from settings import settings
import random

t = Twitter(auth=OAuth(settings['OAUTH_TOKEN'],
                       settings['OAUTH_SECRET'],
                       settings['CONSUMER_KEY'],
                       settings['CONSUMER_SECRET'])
            )


def check_comment_length(comment):
    if len(comment) < 140:
        return comment


def get_comment():
# edit socket url to reflect where you want the bot content to pull from 
    socket = request.Request("http://www.website.com/random/video/", headers={'Cookie': 'age_verified=1'})
    a = request.urlopen(socket)
    soup = BeautifulSoup(a)
    comments = soup.find_all("p", {"class": "message"})
    if comments:
        comment = random.choice(comments)
        if check_comment_length(comment.string):
            return comment.string
        else:
            get_comment()


t.statuses.update(status=get_comment())
