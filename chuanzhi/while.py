# -*- coding: utf-8 -*-

from functools import reduce

# 1-100 的和

def sum100() :
    # sum = reduce(lambda x, y: x + y, range(1,101))
    sum = 0
    i = 1
    max = 101
    while i < max :
        sum += i
        i += 1
    print(sum)

# sum100()



# 1-100 偶数的和
def sumEven() :
    # sum = reduce(lambda x, y: x + y, [x for x in range(1,101) if x % 2 == 0 ])
    sum = 0
    i = 1
    max = 101
    while i < max :
        if i % 2 == 0 :
            sum += i
            i += 2
        else :
            i += 1
    print(sum)

# sumEven()

# 打印星星✨
'''
    ✨
    ✨✨
    ✨✨✨
    ✨✨✨✨
    ✨✨✨✨✨
'''
def printxingxing(n) :
    i = 0
    while i < n:
        j = 0
        while j <= i :
            print('✨ ', end='')
            j += 1
        print('\n')
        i += 1
# printxingxing(6)

# 打印星星2 ✨
'''
    ✨
    ✨✨
    ✨✨✨
    ✨✨✨✨
    ✨✨✨✨✨
    ✨✨✨✨
    ✨✨✨
    ✨✨
    ✨
'''

def printxingxing2(n) :
    if n == 0 : 
        return
    m = 0
    if n % 2 == 0 :
        m = n / 2
    else :
        m = n / 2 + 1
    for i in range(1, n + 1) :
        if i <= m:
            for j in range(0, i) :
                print('✨ ', end='')
        elif i > m:
            for j in range(i, n + 1):
                print('✨ ', end='')
        i += 1
        print('\n')

printxingxing2(0)
