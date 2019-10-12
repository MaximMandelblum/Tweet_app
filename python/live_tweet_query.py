#!/usr/bin/env python

from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient
import sys

host_ip = sys.argv[1]


def queryCollection(host_ip):
    MONGO_HOST = 'mongodb://root:admin@'+host_ip+':27017/admin'
    client = MongoClient(MONGO_HOST)
    print("query tweitter user names")
    db = client.twitterMessagesDocker
    print("List of usernames:\n")
# take json in db and print the username
    for item in db.twitterMessagesDocker.find():
      print(item['user']['name'])

queryCollection(host_ip)
