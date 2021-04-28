from userInfo import UserInfo
import PixelArtGenerator as PAG
import tweepy

user = UserInfo()
auth = tweepy.OAuthHandler(user.consumer_key, user.consumer_secret)
auth.set_access_token(user.access_token, user.access_secret)
PAG.generatePixelImage(PAG.FUNKYFUTURE_x8,50,50,"funkyFuture.png")

api = tweepy.API(auth)

#api.update_with_media("./funkyFuture.png","Testing the random pixel art generation! v2 #testingMyBot #pixel #pixelArt")