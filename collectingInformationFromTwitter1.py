import tweepy
from collectingInformationFromTwitter import OAuthVerifier

def getUserStatistics(user):
        print('\nName : ', user.name)
        print('Screen Name : ', user.screen_name)
        print(' ID : ', user.id)
        print('Account created date and time : ', user.created_at)
        print('Location : ', user.location)
        print('Description : ', user.description)
        print('No. of followers : ', user.followers_count)
        print('No. of friends : ', user.friends_count)
        print('No. of favorite tweets : ', user.favourites_count)
        print('No. of posted tweets : ', user.statuses_count)
        print('Associated url : ', user.url)

def main():
        api = OAuthVerifier()
        user = api.get_user(screen_name="Bisleri1000")
        user1 = api.get_user(screen_name="TST_Offcl")
        user2 = api.get_user(screen_name="David_Billaaaaa")
        getUserStatistics(user2)
        getUserStatistics(user)
        getUserStatistics(user1)

if __name__ == "__main__":
        main() 
