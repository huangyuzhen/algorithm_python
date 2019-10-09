#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
楼梯有n阶，可以一步上1阶，2阶，3阶，问有多少种不同的走法。
n<=1000000
'''

modValue = int(1e9+7)
StepResult = {0:0, 1:1, 2:2, 3: 4}

def floor(n):
    global StepResult

    s = StepResult.get(n)
    if s == None:
        s = floor(n-1) + floor(n-2) + floor(n-3)
        s = s % modValue
        StepResult[n] = s

    return s

x = input("input number: ")
if x != '':
    x = int(x)
    if x > 0:
        for i in range(3, x+1):
            floor(i)

        print(floor(x))
