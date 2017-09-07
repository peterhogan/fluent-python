#from math import sqrt
from cmath import sqrt

class Quadratic(object):

	def __init__(self,a,b,c):
		self.a = a + 0j
		self.b = b
		self.c = c

	def formula(self):
		ps = (-self.b + sqrt(self.b**2-4*self.a*self.c))/2*self.a
		ng = (-self.b - sqrt(self.b**2-4*self.a*self.c))/2*self.a
		return [ps, ng]

	def solve(self):
		if self.a*self.b*self.c == 0:
			self.soln = [None, None]
		try:
			solution = self.formula()	
			for i in [0,1]:
				if solution[i].imag == 0:
					realpart = solution[i].real
					solution[i] = realpart
				self.soln = solution
		except ValueError:
			self.soln = [None, None]
