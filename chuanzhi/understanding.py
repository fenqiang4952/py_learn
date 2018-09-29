# -*- coding: utf-8 -*-

'''
    4、编写程序，完成以下要求：
    提示用户进行输入数据
    获取用户的数据数据（需要获取2个）
    对获取的两个数字进行求和运行，并输出相应的结果
'''
import re

def add(l):
    return int(l[0]) + int(l[1])
a = input('请输入两个数字，用逗号或空格隔开：')
if re.match(r'^(\d*)([\s\,\;]+)(\d*)$', a):
    al = re.split(r'[\s\,\;]+', a)
    if len(al) != 2:
        print('输入不合法,输入两个数字')
    else:
        print('结果是 %d:' % add(al))
else:
    print('输入不合法')