import tweepy
from tweepy import OAuthHandler
import urllib2
from bs4 import BeautifulSoup
import requests
import datetime

import time
import sys
import os

import argparse
import string
import json
import os.path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pickle

consumer_key = 'Gi0rd6bUNcv1GQ2zYJo3XbVC7'
consumer_secret = '3MP591bAfpyF966UDnqrr8wGGMtbxRdKOBd5e8JyAVPjr9YTfb'
access_token = '747983536293052416-uWsP9BxOzPNaSzhpxkBFn3diU7qeW1I'
access_secret = 'AIjtrqCvZLoko6b9oCjUMrUrFF0w9LSdplO19aGMhfnuY'

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.stylesheet', 2)
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
# create driver
driver = webdriver.Firefox(firefox_profile=firefox_profile)
base_url = "https://twitter.com/search?l=en&q=%23{}&src=typd"

class Tweet:
	def __init__(self, id, text, name):
		self.id = id
		self.text = text
		self.name = name
		
def Authenticate():
	auth = OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_secret)
	return auth		

def get_soup(url):
	return BeautifulSoup( requests.get(url).content, 'lxml')

def crawl_page(url, n):
	# open url
	driver.get(url)
	# wait for page to load
	driver.implicitly_wait(15)
	# scroll for n seconds
	for i in range(n):
		elem = driver.find_element_by_tag_name('a')
		elem.send_keys(Keys.END)
		time.sleep(2)
		sys.stderr.write('\r{0}/{1} complete...'.format(i+1,n))
	# gather list items
	list_items = driver.find_elements_by_tag_name('ol')
	# get soup
	soup = BeautifulSoup(list_items[0].get_attribute('innerHTML'),'lxml')
	return soup

def extract_tweet_ids(soup):
	ListaTweets = []
	tweets = soup.find_all('li', 'js-stream-item')
	for tweet in tweets:
		if 'data-item-type' in tweet.attrs and tweet.attrs['data-item-type'] == 'tweet' and tweet.find('p','tweet-text'):
			tweet_id = tweet['data-item-id']
			ListaTweets.append(tweet_id)
	return ListaTweets

def save_tweets(nomeSerie, n, group):
	url = base_url.format(nomeSerie)
	auth = Authenticate()
	api = tweepy.API(auth)
	tweets = []
	# crawl page
	soup = crawl_page(url, n)
	# get tweet tags
	tweetsIds = extract_tweet_ids(soup)
	file = open(nomeSerie + ".json", "w+")
        file.close()
	print('>> Grabbed {0} tweets for {1}'.format(len(tweetsIds), url))
	for i in range(0, len(tweetsIds), 100):
		tweets = []
		try:
			tweets = api.statuses_lookup(tweetsIds[i:i+100])
		except tweepy.RateLimitError:
			time.sleep(15*60)
		except tweepy.TweepError as e:
			print(e)

		for tweet in tweets:
		file = open(nomeSerie + ".json", "a+")
		file.write(json.dumps(tweet._json) + "\n")
		file.close()
		

def ImportTweets(nomeSerie):
    save_tweets(nomeSerie,n=10, group='set3')
    driver.quit()


