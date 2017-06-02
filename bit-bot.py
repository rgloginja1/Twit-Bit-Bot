# sudo pip install feedparser
# sudo pip install bitly_api
# sudo pip install twython
# sudo pip install bitcoin-price-api

from time import gmtime, strftime
from exchanges.bitfinex import Bitfinex

import random
from random import randint

import time
import os

import bitly_api

#Disabled for now - coming soon!
#import feedparser

BITLY_ACCESS_TOKEN = ""

bitly = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)

from TwitterAPI import TwitterAPI

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

woeid = '1'
donate_address = '1HTVj1kV68kyFYxYEqrNfJMyK6xUwJFhFM'

# DO NOT USE BIT.LY ADDRESSES IN THE FAUCET LIST!
faucet_list = ['http://bit.ly/2qFY9Xc','http://bit.ly/162plAB','http://bit.ly/2siuv7F','http://bit.ly/2rfV4fe','http://bit.ly/2ruJj5c']
faucet_choice = (random.choice(faucet_list))

tagged_people = ['@BitcoinAU','@bitcoinprice','@BitcoinBolt','@BitcoinMagazine','@BTCFoundation']

get_result = randint(0,9)
if(get_result <= 4):
	final_string = 'Donate: ' + donate_address
else:
	people_choice = random.choice(tagged_people)
	final_string = "Check out " + people_choice + ' for more news'
	
hashtag_list = ['#entrepreneur','#bizhour','#smallbiz','#developer','#blockchain','#crypto']

x = api.request('trends/place',{'id':woeid})
for item in x:
    if(item['name'][0] == '#'):
		hashtag_list.append(item['name'])

hashtag_choice = random.choice(hashtag_list)


bitcoin_price = Bitfinex().get_current_price()
#current_date = strftime("%H:%M:%S", gmtime())

bit_str = '1BTC = $' + str(format(bitcoin_price,'.2f')) + 'US\n\nFree #Bitcoin: '+str(faucet_choice)+'\n\n#altcoin #startup '+str(hashtag_choice)+'\n\n' + (final_string)

r = api.request('statuses/update', {'status': str(bit_str) })
print 'SUCCESS' if r.status_code == 200 else 'FAILURE' 
