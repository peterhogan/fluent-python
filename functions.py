from operator import mul
from functools import reduce
from math import sqrt

def succ(x):
    return x + 1

def factorial(x):
    if x > 0:
        return reduce(mul, range(1,x+1))
    elif x == 0:
        return 1
    else:
        return ValueError

def mean(l):
    return sum(l)/len(l)

def variance(l):
    l_m = mean(l)
    l2 = [(i-l_m)**2 for i in l]
    return mean(l2)

def sd(l):
    return sqrt(variance(l))

def divisors(n):
    if n == 0:
        return None
    elif n == 1:
        return (1)
    elif n == 2:
        return (2)
    else:
        return tuple(i for i in range(2,n+1) if n%i == 0)

def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n > 2 and len(divisors(n)) == 1:
        return True
    else:
        return False
