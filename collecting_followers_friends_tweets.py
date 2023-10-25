import tweepy
from collectingInformationFromTwitter import OAuthVerifier

def getUserFollowers(api):
        print('\nFollowers:')
        for follower in api.followers():
                print(follower.screen_name)

def getUserFriends(api):
        print('\n Friends:')
        for friend in api.friends():
                print(friend.screen_name)

def getUserTweets(api):
        print('\n Tweets : ')
        for tweet in api.user_timeline():
                print(tweet.text)

def main():
        api = OAuthVerifier()
        getUserFriends(api)
        getUserFollowers(api)

if __name__ == '__main__':
        main()
