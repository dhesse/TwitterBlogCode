#!/usr/bin/env python
from TwitterAPI import TwitterAPI
import pymongo
import argparse
import sys

def auth_collection(db):
    return db.keys

def get_auth(db):
    """Get the Authentication."""
    return auth_collection(db).find_one()

def store_auth(db, auth):
    auth_collection(db).drop()
    auth_collection(db).insert_one(auth)

AUTH_OBJECTS = ("consumer_key", "consumer_secret", "access_token_key", "access_token_secret")

def exit(msg, status):
    print msg
    sys.exit(status)

def auth_from_args(args, db):
    if any((vars(args)[i] for i in AUTH_OBJECTS)):
        if not all((vars(args)[i] for i in AUTH_OBJECTS)):
            exit("You cannot specify authentication info partially!", 1)
        return {k: v for k, v in vars(args).items() if k in AUTH_OBJECTS} 
    else:
        if args.store_auth:
            exit("You have to give auth info in order to store it!", 1)
        return get_auth(db)

def setup(db):
    parser = argparse.ArgumentParser()
    for obj in AUTH_OBJECTS:
        parser.add_argument("--" + obj)
    parser.add_argument("--store_auth", action="store_true")
    parser.add_argument("--track", nargs="+", required=True)
    args = parser.parse_args()
    auth = auth_from_args(args, db)
    if not auth:
        exit("No authentication in MongoDB, and none provided. Exiting.", 1)
    if args.store_auth:
        store_auth(db, auth)
    return auth, args.track

if __name__ == '__main__':
    db = pymongo.MongoClient().twitter
    auth, track = setup(db)
    print "Tracking:", track
    api = TwitterAPI(auth["consumer_key"], auth["consumer_secret"],
                    auth["access_token_key"], auth["access_token_secret"])
    tweet_count = 0
    for i in api.request('statuses/filter',
                          {'track': track,
                           'language': ['en']}).get_iterator():
        db.tweets.insert_one(i)
        tweet_count += 1
        print "{0} Tweets saved.\r".format(tweet_count),
        sys.stdout.flush()
