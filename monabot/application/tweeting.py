
#coding: utf-8
'''
import tweepy
import time

consumer_key = 'bqpEGKxkSLvrIvey783y9zgg7'
consumer_secret = 'oGLqRebTIFcSMYDo8PDFVxXIZj7yfjJUsO1GpB5kq61emvnatW'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
access_token_key = '778308999951167488-1VpIduD2ZNlJz7KEHPoUyQWFWZlrcRa'
access_secret = 'FY8r8iZ2OyLmN7VcL8slznnsIsXHuLntj2X8xZ2QRNvyT'
auth.set_access_token(access_token_key, access_secret)

api = tweepy.API(auth)

def tweet(_tweet) :
	api.update_status(_tweet)
	time.sleep(1)
	return'''
