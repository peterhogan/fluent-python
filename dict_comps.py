from random import betavariate as bv,seed
seed(231012)
letters = 'abcdefghijklmnopqrstuvwxyz'
dict = {i[0]: i[1] for i in ((l,bv(2,1)) for l in letters)}
for i in 'afjow':
    print(dict[i])
