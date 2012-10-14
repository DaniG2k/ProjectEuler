#! /usr/bin/python
result = 0
for i in xrange(2,354294):
  number_to_array = [(int(char)**5) for char in str(i)]
  if sum(number_to_array) == i:
		print i
		result += i
print 'Result:',result
