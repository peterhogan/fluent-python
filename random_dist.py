from random import randrange,uniform as un,betavariate as bv,gauss,gammavariate as gv,sample
from math import sqrt

def mean(l):
    return sum(l)/len(l)

class Random(object):

    def __init__(self,mean, variance, count):
        self.mean = mean
        self.count = count
        self.variance = variance
        self.variables = (un, bv,gauss,gv)
        self.values = tuple((self.variables[randrange(len(self.variables))](self.mean,self.variance) 
            for i in range(self.count)))

    def __str__(self):
        mean = self.getmean()
        return "Real Mean:"+str(mean)

    def getmean(self):
        self.realmean = sum(self.values)//len(self.values)
        return self.realmean

    def getsample(self,k):
        self.sample = sample(self.values,k)
        return self.sample

    def getvariance(self):
        mn = self.getmean()
        diffs = tuple(((i - mn)**2 for i in self.values))
        self.realvariance = mean(diffs)
        self.sd = sqrt(self.realvariance)
        return self.realvariance
