from collections import namedtuple

Quadratic = namedtuple('Quadratic', 'a b c')
q = Quadratic(1,2,3)
print(q)
print(q.a)
print(q.c)
print(q[1])
