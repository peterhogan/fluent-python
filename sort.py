import bisect
from random import randrange
from random import random
from time import sleep
r_list = []
for i in range(10):
    num = str(10*random())[:5]
    bisect.insort(r_list, num)
    print('%5r :' % num, r_list)
    sleep(0.1)
