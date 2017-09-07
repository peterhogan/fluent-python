from graphics import *
from random import random
from time import sleep

win = GraphWin()
pt = Point(100,100)
pt.draw(win)

while True:
    pt.move(random()-0.5,random()-0.499)
    #sleep(0.01)
