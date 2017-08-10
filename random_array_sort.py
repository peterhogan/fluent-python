from random import random
from array import array
from time import time,sleep
from sys import argv
import bisect

LIMIT = 10**int(argv[1])
start = time()

randl = array('d')
for i in range(LIMIT):
    num = round(random()*100,2)
    bisect.insort(randl, num)
    print('%3r' % round(100*i/LIMIT)+'%', end='\r')
    #print('%5r :' % num, randl)
print(randl[0],randl[-1])
print("Time:",time()-start,"seconds")
