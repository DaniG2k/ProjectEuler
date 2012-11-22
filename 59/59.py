#!/usr/bin/python

with open('cipher1.txt', 'r') as f:
    data = f.read()

data = data.strip('\n ').split(',')

