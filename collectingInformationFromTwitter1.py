import tweepy
from collectingInformationFromTwitter import OAuthVerifier

def getUserStatistics(user):
        print('\nName : ', user.name)

def main():
        api = OAuthVerifier()
        user = api.get_user(screen_name="Bisleri1000")
        getUserStatistics(user)

if __name__ == "__main__":
        main() 
