#! /usr/bin/python
def unique(seq):
	seen = set()
	return [x for x in seq if x not in seen and not seen.add(x)]

seq = []
for a in xrange(2,101):
	for b in xrange(2,101):
		seq.append(a**b)

print len(unique(seq))