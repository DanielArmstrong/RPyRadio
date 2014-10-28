# start: python radio.py
#
# Simple internet radio station Python script using mpg123 http://www.mpg123.org/
# Python 2.7 / RaspberryPi
# 
# Add your favourite radio stations to stations.txt (___ = tab)
# one per line, in the following format:
# id Name___url of mp3 stream
#

import os           # used to clear display
import subprocess   # used to start another program (mpg123)

# open file and split by lines
f = open('stations.txt','r')
lines = f.readlines()
f.close()

# setup stations and urls arrays
stations = []
urls = []
for line in lines:
	split = line.split("\t")
	stations.append(split[0].strip("\n"))
	urls.append(split[1].strip("\n"))

# print stations (on Adafruit PiTFT, console)

def display(list):
	os.system('cls' if os.name == 'nt' else 'clear')
	print "----------------------=[RpyRadio v1.0]=-"
	print ""
	x = -1
	second = ""
	for k in list:
		x=x+1
		if x == 0:
			print "", list[0][0:17].ljust(18), "." , list[1][0:17].ljust(18)
			continue
		if x == 1:
			continue
		if x % 2 == 0:
			second = k
			continue
		print "", second[0:17].ljust(18), "." , k[0:17].ljust(18)
		second = ""
	print ""
	print "----------------------------------------"
	return

keepasking=1

while keepasking == 1:
	display(stations)
	station = input('Enter Station #ID: ')
	if station > len(stations):
		continue
	if station < 0:
		continue
	keepasking=0

os.system('cls' if os.name == 'nt' else 'clear')

# start mpg123
cmdline = ['mpg123', urls[station-1].strip("\n")]
if os.name == 'nt':
	cmdline = ['c:\\Python27\\mpg123\\mpg123.exe', urls[station-1].strip("\n")]

subprocess.call(cmdline)
