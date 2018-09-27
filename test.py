from math import pi
from until.until import findMinAndMax
import functools
import time
import os
import datetime
from enum import Enum
# a = [66.25, 333, 333, 1, 1234.5]

# for i, value in enumerate(a):
#     print(i, value)

# print(a.count(333))

# print([(x, x**2) for x in range(6)])

# print([str(round(pi, i)) for i in range(1,6)])

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]

# print(list(zip(*matrix)))

# L = []
# for x in range(1,11):
#     L.append(x*x)

# L = ( x * x for x in range(1, 11) if x % 2 == 0 )
# L = [d for d in os.listdir('.')]
# print(next(L))


# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# for k, v in d.items():
#     print(k, v)

# L1 = ['Hello', 'World', 18, 'Apple', None]

# L2 = [x for x in L1 if isinstance(x, str)]

# print(L2)

# s = 'asUsdT'

# print(s.lower().capitalize())
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw): 
#         print('%s executed in %s ms' % (fn.__name__, time.localtime().tm_year+time.localtime().tm_year))
#         return fn(*args, **kw)
#     return wrapper


# L = [3, 5, 7, 9]

# @metric
# def prod(L):
#     return functools.reduce(lambda x, y: x*y, L )

# print(prod(L))

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print(name , member.name)
# print(isinstance(Month.Jan.name, str))

# print('Process (%s) start...' % os.getpid())

print(datetime.datetime.now().timestamp())

print(datetime.datetime.fromtimestamp(1537980094.493515))