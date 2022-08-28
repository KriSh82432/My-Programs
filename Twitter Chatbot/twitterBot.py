import tweepy as tw

consumer_key = 'Ok1xDZEqom7j1xOsP7IBIO2Lg'
consumer_secret = 'stsXDRFETK1qzV9Qhln0wlU7xCMntwbeouUeyeaMmw9fx9DHGp'
access_token = '1560290499759833088-t5n8qFmDPLdar3vqHuYIEivpIovl9A'
access_token_secret = '1P5rE739d5Y7nU5d9l6onDg6YOwtDKqrl1PN7JeoY3hTJ'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

user = api.verify_credentials()

print(user.name)
print(user.screen_name)
print(user.followers_count)

for friend in user.friends():
    print(friend.name)

for follower in user.followers():
    print(follower.name)

# Search for tweets
tweets = api.search_tweets('#14YearsOfViratKohli')
print("Tweets: " + str(len(tweets)))
for tweet in tweets:
    print(tweet.text)

#   Get likes of tweets
tweets = api.search_tweets('#14YearsOfViratKohli')
print("Likes of tweets:")
for tweet in tweets:
    print(tweet.favorite_count)

#   Get retweets of tweets
tweets = api.search_tweets('#14YearsOfViratKohli')
print("Retweets of tweets:")
for tweet in tweets:
    print(tweet.retweet_count)