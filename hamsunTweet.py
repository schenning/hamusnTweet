#!/usr/bin/env python
# -*- coding: utf-8 -*-

# written by Schenning 

import tweepy, time, random


CHARS = 160



CONSUMER_KEY = 
CONSUMER_SECRET = 
ACCESS_KEY = 
ACCESS_SECRET =
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('lines.txt','r')
f=filename.readlines()
filename.close()

def cnt(string):
	return len(string)





def rnd(mi, ma):
	t=random.randrange(mi,ma)
	if t>=0 and t<=3600:
		return t
	else:
		return 14 
	




#api.update_status('Mye arti man kan gjøre på internett. Her kommer hele Knut Hamsuns' 'Sult'' på Twitter. Heng med! ')
#time.sleep(10)
for line in f:
     api.update_status( '@yourTwitterName' + line)
     print line
     time.sleep(rnd(0,36)) # Sleep for random amount of time between 0 and 3600 seconds





