from tools import fib
from time import time
start = time()

print sum([even for even in fib(4000000) if even%2==0])

end = time()
print end-start
