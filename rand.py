from random import randint
from time import sleep
def main():
	print('Start')
	lst = []
	for i in range(1000):
		rnd = randint(0,100)
		lst.append(rnd)
		avg = sum(lst)/len(lst)
		print("val:\t",randint(0,100),"\tavg:\t",str(avg)[:5],"\titer:\t",i, end='\r')
		sleep(0.03)
	print('Done')

main()
