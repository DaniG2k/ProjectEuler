#! /usr/bin/python
f = open('roman.txt', 'r')
full_size = ''
reduced_size = ''

for n in f:
    n = n.strip()
    full_size += n
    # The replacement needs to occur in descending order
    n = n.replace('DCCCC', 'CM') #900
    n = n.replace('CCCC', 'CD') #400
    n = n.replace('LXXXX', 'XC') #90
    n = n.replace('XXXX', 'XL') #40
    n = n.replace('VIIII', 'IX') #9
    n = n.replace('IIII', 'IV') #4
    reduced_size += n
f.close()

print len(full_size)-len(reduced_size)
