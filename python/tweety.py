#!/usr/bin/env python

from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient
import sys

host_ip = sys.argv[1]


MONGO_HOST = 'mongodb://root:admin@'+host_ip+':27017/admin'

# which words to track
WORDS = ['#docker', 'docker', '#Docker','Docker']

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# app path
with open('/home/centos/twitterapp/index.html', 'a') as the_file:
    the_file.write("Results of tweets that contain docker word:")
    the_file.write('<br>')


class StreamListener(tweepy.StreamListener):

    def on_connect(self):
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        try:

            client = MongoClient(MONGO_HOST)
            # Use twitterMessagesDocker database
            db = client.twitterMessagesDocker

            # Decode the JSON from Twitter
            datajson = json.loads(data)

            # grab the created_at , content_of_tweet , username_in_tweeter data from the Tweet to use for display
            created_at = datajson['created_at'].encode("utf-8")
            content_of_tweet = datajson['text'].encode("utf-8")
            # check that exist docker in msg
            if ("docker" not in content_of_tweet) and ("Docker" not in content_of_tweet) and (
                    "#docker" not in content_of_tweet) and ("#Docker" not in content_of_tweet):
                print("Error , docker not in tweet!")
                exit(1)
            username_in_tweeter = datajson['user']['screen_name'].encode("utf-8")
            # print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created_at) + " , From user:" + str(username_in_tweeter) + " , The Tweet content: " + str(content_of_tweet))
            msg = "Tweet collected at " + str(created_at)+ " , From user:"+ str(username_in_tweeter) + " , The Tweet content: " + str(content_of_tweet)
            with open('/root/myapp/index.html', 'a') as the_file:
               the_file.write(msg)
               the_file.write('<br>')
            # insert the data into the mongoDB into a collection called twitterMessagesDocker
            db.twitterMessagesDocker.insert(datajson)

        except Exception as e:
            print(e)


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)
