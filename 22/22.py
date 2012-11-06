#! /usr/bin/python
#from time import time
#start = time()

f = open('./names.txt')
n = f.read()
n = n.split(',')
alphabet = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5,
	'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11,
	'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17,
	'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23,
	'X':24, 'Y':25, 'Z':26}


def sort_names(names):
	l = [name[1:-1] for name in names] # Remove double quotes
	l.sort() # Sort the new list
	return l

def letters_score(name):
	score = [alphabet[letter] for letter in name]
	return sum(score)

def word_score(lscore, listnum):
	return lscore * listnum

names = sort_names(n)
listnum = 1
total_score = []
for name in names:
	total_score.append( word_score(letters_score(name), listnum) )
	listnum += 1

print sum(total_score)

#end = time()
#print 'Time elapsed:',end-start
