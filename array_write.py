import array as ar
from random import random
from time import time
start = time()
floats = ar.array('d', (random() for i in range(10**7)))
print("Time taken making array:",time()-start)
start = time()
#fp = open('floats.bin','wb')
fp = open('floats-10M-lines.txt','w')
for i in floats:
    fp.write(str(i)+'\n')
#floats.tofile(fp)
fp.close()
'''
print("Time taken writing array:",time()-start)
floats2 = ar.array('d')
fp = open('floats-10M-lines.txt','rb')
floats2.fromfile(fp,10**7)
print("Time taken reading array:",time()-start)
fp.close()
print(floats2[-1])
'''
print("Total time taken:",time()-start)
