# Yuxuan Chen
# yuxuanc


# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here
# usage should be python3 part1.py <username> <num_tweets>


# Helper functions
# find freequency of words
def word_counter(list_of_words):
    unique_words = set(list_of_words)
    output = []
    if len(unique_words) < len(list_of_words):
        for word in unique_words:
            freq = (word, list_of_words.count(word))
            output.append(freq)
    return output

# sort by frequency and alphabetically
def sort_list(input_list):
    return sorted(input_list, key=lambda x: (-x[1], x[0]))

# print top 5 words and counts
def print_top_5(part_of_speech, input_list):
    output = part_of_speech
    for i in range(5):
        output += " " + input_list[i][0] + "(" + str(input_list[i][1]) + ")"
    print(output)



# twitter access stuff taken from my code from SI 206 when I took it in Fall 2016
access_token = "36809399-VDjgUVFRUnpzZmcuFTq2Vbulo12NpuS4rFWf2oK94"
access_token_secret = "jntNnLofnovHDGlI5Dju2NJaQALvVNM3tcCXVTrIMGtrn"
consumer_key = "klvXTbx7MFMCge2QpCdsyDTKc"
consumer_secret = "xpVdUfqXh1IoEsxGCvDEatfZLXYdJoyKl1hFR7g7I1b73GArlP"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

# get argv info
username = sys.argv[1]
num_tweets = sys.argv[2]

# get tweets and a list of words to analyze
word_list = []
tweets = api.user_timeline(id=username, count=num_tweets, tweet_mode="extended")
for tweet in tweets:
    # print(tweet._json["full_text"])
    tokenized_tweet = nltk.tokenize.word_tokenize(tweet._json["full_text"])
    for token in tokenized_tweet:
        if token[0].isalpha() and token not in ['http', 'https', 'RT']:
            word_list.append(token)

# analyze words
tagged = nltk.pos_tag(word_list)
verbs = []
nouns = []
adjectives = []

for word in tagged:
    if word[1].startswith("VB"):
        verbs.append(word[0])
    elif word[1].startswith("NN"):
        nouns.append(word[0])
    elif word[1].startswith("JJ"):
        adjectives.append(word[0])

# find freequency of words
verbs = word_counter(verbs)
nouns = word_counter(nouns)
adjectives = word_counter(adjectives)

# sort by frequency and alphabetically
verbs = sort_list(verbs)
nouns = sort_list(nouns)
adjectives = sort_list(adjectives)


og_tweets = 0
num_favs = 0
retweets = 0
for tweet in tweets:
    if not tweet._json["retweeted"]:
        og_tweets += 1
        num_favs += tweet._json["favorite_count"]
        retweets += tweet._json["retweet_count"]


# print everything
print("USER:", username)
print("TWEETS ANALYZED:", num_tweets)
print_top_5("VERBS:", verbs)
print_top_5("NOUNS:", nouns)
print_top_5("ADJECTIVES:", adjectives)
print("ORIGINAL TWEETS:", og_tweets)
print("TIMES FAVORITED (ORIGINAL TWEETS ONLY):", num_favs)
print("TIMES RETWEETED (ORIGINAL TWEETS ONLY):", retweets)

# save top 5 nouns to csv file
with open('noun_data.csv', 'w+') as f:
    print("Noun", "Number", file=f, sep=",")
    for i in range(5):
        print(nouns[i][0], nouns[i][1], file=f, sep=",")