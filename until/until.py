# -*- coding: utf-8 -*-

def findMinAndMax(L):
    # 找出一个数组的最大值和最小值
    min = L[0]
    max = L[0]
    for item in L:
        if item > max:
            max = item
        elif item < min:
            min = item
    return (min, max)
        