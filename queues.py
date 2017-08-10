from collections import deque
from time import sleep
from random import betavariate,normalvariate,randint
from os import system


FRMT = '>> {0:2d} ||  {1:2d}   {2:2d}   {3:2d}   {4:2d}   {5:2d}   {6:2d}   {7:2d}   {8:2d}   {9:2d}'
#FRMT = '{0:1f} {1:1f} {2:1f} {3:1f} {4:1f} {5:1f} {6:1f} {7:1f} {8:1f} {9:1f}'
q1 = deque((abs(int(normalvariate(0,9)))+1 for i in range(10)))
#print(FRMT.format(1,2,3,4,5,6,7,8,9,10))
while True:
    print('-'*100)
    #print(FRMT.format(q1[0],q1[1],q1[2],q1[3],q1[4],q1[5],q1[6],q1[7],q1[8],q1[9]))
    for i in range(len(q1)):
        print(q1[i], end='\t')
        #print('#', end=' ')
    print('')
    print('-'*100)
    if len(q1) > 0:
        q1[0] -= 1
    flip = randint(0,10)
    if flip == 0:
        q1.append(abs(int(normalvariate(0,9)))+1)
    sleep(0.2)
    system('clear')
    while 0 in q1:
        q1.remove(0)
