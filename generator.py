from random import gammavariate as gv
import reprlib

class gammarange():
    def __init__(self, alpha, beta, lower, upper):
        self.alpha = alpha
        self.beta = beta
        self.lower = lower
        self.upper = upper

    def __repr__(self):
        return reprlib.repr("Gamma Variate")

    def 
