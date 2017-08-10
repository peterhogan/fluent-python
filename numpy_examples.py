import numpy
from time import time,perf_counter
start = time()
floats = numpy.loadtxt('floats-10M-lines.txt')
print("Time:",time()-start)
print(floats[-3:])
floats *= .5
print(floats[-3:])
t0 = perf_counter()
floats /= 3 
print("Time:",perf_counter() - t0)
start = time()
numpy.save('floats-10M', floats)
print("Time:",time()-start)
