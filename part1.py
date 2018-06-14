# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here
# usage should be python3 part1.py <username> <num_tweets>

# taken from my code from SI 206 when I took it in Fall 2016
access_token = "36809399-VDjgUVFRUnpzZmcuFTq2Vbulo12NpuS4rFWf2oK94"
access_token_secret = "jntNnLofnovHDGlI5Dju2NJaQALvVNM3tcCXVTrIMGtrn"
consumer_key = "klvXTbx7MFMCge2QpCdsyDTKc"
consumer_secret = "xpVdUfqXh1IoEsxGCvDEatfZLXYdJoyKl1hFR7g7I1b73GArlP"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

username = sys.argv[1]
num_tweets = sys.argv[2]
tweets = api.search(username)


print("USER", username)
print("TWEETS ANALYZED:", num_tweets)
# print("VERBS:", verbs)
# print("NOUNS:", nouns)
# print("ADJECTIVES", adjectives)
# print("ORIGINAL TWEETS:", og_tweets)
# print("TIMES FAVORITED (ORIGINAL TWEETS ONLY):", num_favs)
# print("TIMES RETWEETED (ORIGINAL TWEETS ONLY):", retweets)
# with open() as f:
#     Noun,Number