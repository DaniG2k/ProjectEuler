#! /usr/bin/env python

#If all the numbers from 1 to 1000 (one thousand) inclusive
#were written out in words, how many letters would be used?

counters = {1: 'one', 2: 'two',
			3: 'three', 4: 'four',
			5: 'five', 6: 'six',
			7: 'seven', 8: 'eight',
			9: 'nine', 10: 'ten',
			11: 'eleven', 12: 'twelve',
			13: 'thirteen', 14: 'fourteen',
			15: 'fifteen', 16: 'sixteen',
			17: 'seventeen', 18: 'eighteen',
			19: 'nineteen', 20: 'twenty',
			30: 'thirty', 40: 'forty',
			50: 'fifty', 60: 'sixty',
			70: 'seventy', 80: 'eighty',
			90: 'ninety'
			}

words = []

for n in xrange(1,1001):
	if n <= 20:
		#print counters[n]
		words.append(counters[n])
	elif n == 1000:
		#print 'one thousand'
		words.append('one thousand'.replace(' ',''))
	elif 100 > n > 20:
		if n % 10 == 0:
			#print counters[n]
			words.append(counters[n])
		else:
			s = str(n)
			tens = s[0] + '0'
			ones = s[1]
			#print counters[int(tens)], counters[int(ones)]
			words.append(counters[int(tens)])
			words.append(counters[int(ones)])
	elif 1000 > n >= 100:
		s = str(n)
		hundreds = s[0]
		if n % 100 == 0:
			#print counters[int(hundreds)],'hundred'
			words.append(counters[int(hundreds)])
			words.append('hundred')
		else:
			tens = s[1:]
			ones = s[2]
			words.append(counters[int(hundreds)])
			words.append('hundred and'.replace(' ',''))
			if tens == '00':
				#print counters[int(hundreds)],'hundred','and',counters[int(ones)]
				words.append(counters[int(ones)])
			elif int(tens) in counters:
				#print counters[int(hundreds)],'hundred','and',counters[int(tens)]
				words.append(counters[int(tens)])
			else:
				tens = tens[0] + '0'
				#print counters[int(hundreds)],'hundred','and',counters[int(tens)],counters[int(ones)]
				words.append(counters[int(tens)])
				words.append(counters[int(ones)])

print len(''.join(words))
