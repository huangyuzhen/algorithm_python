#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
收集控的决策问题
自底向上计算
'''

n = int(input(""))

for i in range(n):
    line2 = input("").split()
    num = int(line2[0])
    capacity = int(line2[1])

    value = []
    weight = []

    line3 = input("").split()
    line4 = input("").split()
    for i in range(num):
        value.append(int(line3[i]))
        weight.append(int(line4[i]))


#  P[0],...,P[capacity]
P = [0] * (capacity+1)
for n in range(1, capacity+1):
    maxV = 0
    for i in range(num):
        w = weight[i]
        v = value[i]
        if n >= w:
            m = P[n-w] + v
            maxV = max(maxV, m)

    P[n] = maxV

print(P[capacity])

