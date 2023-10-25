import tweepy
from collectingInformationFromTwitter import OAuthVerifier

def getUserFollowers(api):
        print('\nFollowers:')
        for follower in tweepy.cursor(api.followers()).items():
                print(follower.screen_name)

def getUserFriends(api):
        print('\n Friends:')
        for friend in tweepy.cursor(api.friends()).items():
                print(friend.screen_name)

def getUserTweets(api):
        print('\n Tweets : ')
        for tweet in tweepy.cursor(api.user_timeline()).items():
                print(tweet.text)

def main():
        api = OAuthVerifier()
        getUserFriends(api)
        getUserFollowers(api)

if __name__ == '__main__':
        main()
