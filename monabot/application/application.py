
# coding: utf-8

import io
import sys
import socks
import time
import codecs
import re
#import tweeting
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='cp932', errors='replace') # output -> cp932

### host infomation ################################################################################################################
host_addr = 'monachat.dyndns.org' # host address																				   #
host_port = 9095 # host port number																								   #									  
####################################################################################################################################

### proxy infomation ###############################################################################################################
proxy_addr = '179.159.203.35' # proxy address																					   #																	  
proxy_port = 49688 # proxy address																								   #
####################################################################################################################################

### bot infomation #################################################################################################################
room = 5 # room number																											   #																								  
name = 'SPiCa'.encode('utf-8') # name																							   #
ihash = '未設定(設定不可)'.encode('utf-8') # ihash																				   #
trip = 'ihash'.encode('utf-8') # trip																							   #
char = 'miwa'.encode('utf-8') # char																						       #
red = 100 # red color																											   #
green = 40 # green color																								           #
blue = 40 # blue color																										       #
x = 150 # x positon																												   #
y = 0 # y position																											       #
scl = 100 # muki																												   #
stat = '通常'.encode('utf-8') # status																							   #
####################################################################################################################################

####################################################################################################################################
buffer = 1024 # buf size																										   #
time_t = time.time() # get localtime																							   #
send_t = time_t + 20 # send time																								   #
response = 'none'.encode('utf-8')																								   #
#tweet_pattern = re.compile('<COM cmt="([^"]+?)\s+/tweet".*/>')																	   #
#tweet_data = 'none'																											   #
####################################################################################################################################

### int -> bytes ###################################################################################################################
room.to_bytes(2, 'big') # room int -> bytes																						   #																		  
red.to_bytes(2, 'big') # red int -> bytes																					       #
green.to_bytes(2, 'big') # green int -> bytes																					   #  
blue.to_bytes(2, 'big') # blue int ->bytes																					       #
x.to_bytes(2, 'big') # x int -> bytes																					           #
y.to_bytes(2, 'big') # y int -> bytes																							   #
scl.to_bytes(2, 'big') # scl int -> bytes																						   #  
####################################################################################################################################

sophia = socks.socksocket() # make socket																								  
sophia.set_proxy(socks.SOCKS5, proxy_addr, proxy_port) # set proxy 											  
sophia.connect((host_addr, host_port)) # connect server																					  
sophia.send(b'MojaChat\0') # connect monachat																										  
sophia.send(b'<ENTER room="/MONA8094/%d" Name="%s" IHASH="%s" Trip="%s" type="%s" r="%d" g="%d" b="%d" \
x="%d" y="%d" scl="%d" stat="%s" />\0' % (room, name, ihash, trip, char, red, green, blue, x, y, scl, stat)) # enter room

'''def twitter() :
	iterator = tweet_pattern.finditer(response.decode())

	for match in iterator :
		global tweet_data
		if(tweet_data == match.group(1)) :
			time.sleep(1)
			sophia.send(b'<COM Cmt="Failed to send tweet on Twitter" />\0')
			return
		tweeting.tweet(match.group(1))
		sophia.send(b'<COM Cmt="Succeed to send tweet on Twitter" />\0')
	else :
		tweet_data = match.group(1)
	return'''

def reenter() :
	time.sleep(1)
	sophia.send(b'<EXIT id="%s" />\0' % ihash)
	sophia.send(b'<ENTER room="/MONA8094/%d" Name="%s" IHASH="%s" Trip="%s" type="%s" r="%d" g="%d" b="%d" x="%d" y="%d" scl="%d" stat="%s" />\0' \
	% (room, name, ihash, trip, char, red, green, blue, x, y, scl, stat))

while True :
	time_t = time.time() # update time

	if send_t < time_t :
		sophia.send(b'<NOP />\0')
		send_t = time_t + 20

	response = sophia.recv(buffer)
	print(response.decode(), flush = True)

	#twitter()

	if(b'/reenter' in response) :
		reenter()