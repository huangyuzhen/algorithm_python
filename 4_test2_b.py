#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
收集控的决策问题
自底向上
O(nC)
'''

def getMaxValue(Num, Capacity, Weight, Value):
    V = [0] * (Capacity+1)
    for p in range(1, Capacity+1):
        maxV = 0
        for i in range(Num):
            w = Weight[i]
            if p >= w:
                m = V[p-w] + Value[i]
                maxV = max(maxV, m)
        V[p] = maxV

    return V[Capacity]


n = int(input(""))

for i in range(n):
    line1 = input("").split()

    num = int(line1[0])
    cap = int(line1[1])

    value  = []
    weight = []

    line2 = input("").split()
    line3 = input("").split()
    for i in range(num):
        value.append(int(line2[i]))
        weight.append(int(line3[i]))

    value = getMaxValue(num, cap, weight, value)
    print(value)
