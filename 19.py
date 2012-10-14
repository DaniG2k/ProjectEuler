#! /usr/bin/env python

#How many Sundays fell on the first of the month during the
#twentieth century (1 Jan 1901 to 31 Dec 2000)?

months = [['Jan', 31],
		['Feb', 28],
		['Mar', 31],
		['Apr', 30],
		['May', 31],
		['Jun', 30],
		['Jul', 31],
		['Aug', 31],
		['Sep', 30],
		['Oct', 31],
		['Nov', 30],
		['Dec', 31]]

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

years = [i for i in xrange(1900, 2001)]

def leapYear(y):
	if y % 4 == 0:
		if y % 400 == 0:
			return True
		elif y % 100 == 0:
			return False
		else:
			return True
	else:
		return False
		
i, sundayCounter = 0, 0

for year in years:
	#print year
	if leapYear(year):
		months[1][1] = 29
	else:
		months[1][1] = 28
	for num in months:
		#print num[0]
		for num in xrange(1,num[1] + 1):
			if i > 6:
				i = 0
			#print (num,days[i]),
			if num == 1 and days[i] == 'Sun' and year != 1900:
				sundayCounter += 1
			i += 1
		#print '\n'

print sundayCounter
