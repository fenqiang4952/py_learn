from math import pi
a = [66.25, 333, 333, 1, 1234.5]


print(a.count(333))

print([(x, x**2) for x in range(6)])

print([str(round(pi, i)) for i in range(1,6)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(list(zip(*matrix)))