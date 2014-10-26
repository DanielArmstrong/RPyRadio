# start: python radio.py
#
# Simple internet radio station Python script using mpg123 http://www.mpg123.org/
# Python 2.7 / RaspberryPi
# 
# Add your favourite radio stations to stations.txt (___ = tab)
# one per line, in the following format:
# id Name___url of mp3 stream
#
import subprocess
f = open('stations.txt','r')
lines = f.readlines()
f.close()
# print len(lines) # number of items in array
x=0
while x < len(lines):
	print lines[x].strip("\n")
	x=x+1
station = input('Enter Station #ID: ')
print "Selected Station station #ID: ", station
str = lines[station-1]
print str
url = str.split("\t");
# print "test: ", url[1].strip("\n")
cmdline = ['mpg123', url[1].strip("\n")]
subprocess.call(cmdline)
