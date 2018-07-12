import os
from multiset import BaseMultiset
cwd = os.getcwd()
sl = open(cwd + '/sortedList')
anagram = input("Enter Anagram: ")
anagramSet = BaseMultiset.__init__(anagram)
anagramLen = len(anagram)

contins = True

#print list(anagramSet)

def isSublist(sublist,mainlist):
	for item in sublist:
			contains = True
			if sublist.issubset(mainlist):
				contains = True
			else:
				contains = False
				break
	return contains


for line in sl:
	if len(line) > anagramLen:
		break
	#print line
	lineSet = multiset(line)
	if isSublist(anagramSet,lineSet) is True:
		print( '\t' + line)

