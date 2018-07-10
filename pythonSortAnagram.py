#!/usr/bin/python
import os
fo = open('/home/uit/Projects/american-english', "r")
sl = open('/home/uit/Projects/sortedList', 'a')
buffFile = open('/home/uit/Projects/buffFile', 'a')
x = 4
while x < 25:
	y = 1
	#print 'helpa'
	for line in fo:
		#print 'dddas'
		#print len(line)
		#print x
		if r"'" not in line:
			if len(line) == x :
				sl.write(line)
				#print x
				#print x
				#print x
				#print x
		y = y + 1
	x = x + 1
	fo.seek(0)


buffFile.close()
sl.close()
fo.close()