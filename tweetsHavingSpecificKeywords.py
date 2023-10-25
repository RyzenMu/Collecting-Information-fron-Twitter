import tweepy
from collectingInformationFromTwitter import OAuthVerifier

class MyStreamListener(tweepy.StreamListener):
        def on_status(self, status):
                print(status.text)
        def on_error(self, status)::
                if status == 420:
                        return False

def main():
        api = OAuthVerifier()
        listenerOb = MyStreamListener()
        myStream = tweepy.Stream(api.auth, listenerOb)
        searchList = eval(input('Enter search keyword list : '))
        myStream.filter(track = searchList)

if __name__ == '__main__':
        main()
