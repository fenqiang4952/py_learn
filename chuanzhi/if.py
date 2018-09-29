# -*- coding: utf-8 -*-
import random

player = input('请输入：剪刀(0)  石头(1)  布(2):')

player = int(player)

computer = random.randint(0,2)

if (computer == 0 and player == 1) or (computer == 1 and player == 2) or (computer == 2 and player == 0) :
    print('你赢了！')
elif computer == player :
    print('平局!')
else :
    print('你输了')