from itertools import product
from random import shuffle
whitesuits = (u'\u2664',u'\u2661',u'\u2662',u'\u2667')
blacksuits = (u'\u2660',u'\u2665',u'\u2666',u'\u2663')
cardvalues = tuple(map(str,range(2,11)))+tuple('JQKA')
blackdeck = list(product(cardvalues,blacksuits))
whitedeck = list(product(cardvalues,whitesuits))
shuffle(blackdeck)
fmt = '{:>2}{:1s}'
for i in range(10):
    card = blackdeck.pop()
    print(fmt.format(card[0],card[1]))
