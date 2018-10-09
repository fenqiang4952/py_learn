# -*- coding: utf-8 -*-
import random

# A = ['xiaoWang','xiaoZhang','xiaoHua']

# B = ['x', 'y', 'z']

# A.append('add')

# A.extend(B)

# C = A + B

# count = A.count('xiaoWang')
# index = A.index('xiaoZhang')

# _in = 'xiaoWang' not in A

# A.reverse()
# print(A)

offices = [[],[],[]]

names = ['A','B','C','D','E','F','G','H']

for teacher in names:
    random.choice(offices).append(teacher)

# print(offices)

# print(random.choice(offices))

# a = 1
# b = 2

# (a,b) = (b,a)

# print(a)

# lista = [1,4,7,8,90,34]

# print(min(lista))

# stra = 'hello world'

# sumd = {}

# for x in stra:
#     if x.isspace() :
#         continue
#     if x in sumd:
#         sumd[x] += 1
#     else :
#         sumd[x] = 1

# print(sumd)

# a = 1
# def f():
#     a += 10
#     print(a)
# f()

# list_a = [1, 2]
# print(id(list_a))
# def selfAdd(a):
#     a += a 
#     print(id(a))

# selfAdd(list_a)

# print(list_a)

# a = 1
# b = a
# a += 2

# print(a,id(a),b,id(b))

for x in range(1, 10):
    for y in range(1, x + 1):
        print('%d * %d = %s'%(y,x,str(y*x).ljust(2)), end='  ')
    print(' ')