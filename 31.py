#! /usr/bin/python
#Needed this to help with solution.
#http://www.algorithmist.com/index.php/Coin_Change

limit = 200
coins = [1,2,5,10,20,50,100,200]
grid = [1]+[0]*limit

for coin in coins:
	for n in xrange(coin, limit+1):
		grid[n] += grid[n-coin]
print grid[limit]

