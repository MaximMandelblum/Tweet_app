#!/usr/bin/env python

from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient
import sys

#connect
host_ip = sys.argv[1]

def createCollection(host_ip):
    MONGO_HOST = 'mongodb://root:admin@'+host_ip+':27017/admin'
    client = MongoClient(MONGO_HOST)
    print("Creating now twitter capped collection")
    db = client.admin
#create capped collection
    db.create_collection('twitterMessagesDocker', capped=True, size=2000)

createCollection(host_ip)
