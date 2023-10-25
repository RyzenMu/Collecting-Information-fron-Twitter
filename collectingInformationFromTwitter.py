# twitter provides two Api#1. Streaming Api
#2. Rest Api

api_key = "71ZbqEtWnPGnl7PyOGynyOEtQ"
api_secret_key = "V1d4wcrQVKbmUPKmT3G7vRXGOtQlQECnlHtIt11kyC0WA501Nc"

bearer_token = "AAAAAAAAAAAAAAAAAAAAAIy1qgEAAAAAzcLxTi8s1HStua%2BqomECoXtuGT8%3Dk2vwkBArmqxMrNbhx4ff1oKNX527IlvgOYZqUhqHwRtQKYLwOQ"

access_token = "1716769436403630080-uosHQt7O46ej7fmr9NnaQ4ScofLVAn"

access_token_secret = "P8JdFQZLSWqwQBD89j8Or7LrSBuh2jnzluLz74Di5cFfh"

import tweepy

def OAuthVerifier():
        authorization = tweepy.OAuthHandler(api_key, api_secret_key)
        authorization.set_access_token(access_token, access_token_secret)
        api = tweepy.API(authorization)
        return api

def main():
        api = OAuthVerifier()
        print('application authorized')
  
if __name__ == "__main__":
        main()
