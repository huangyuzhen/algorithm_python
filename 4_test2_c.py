#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
收集控的决策问题
贪心算法
利用优先队列处理排序
O(n)
'''

from queue import PriorityQueue as PQueue

class CompareAble:
    def __init__(self, w, v):
        self.weight = w
        self.value  = v
        self.rate   = v / w

    # 这里是按python3语法，定义的 < 方法
    def __lt__(self, other):
        if self.rate >= other.rate:
            return True
        else:
            return False


def getMaxValue(Num, Capacity, Weight, Value):
    pq = PQueue()
    for i in range(Num):
        item = CompareAble(Weight[i], Value[i])
        pq.put(item)

    cap = Capacity
    maxV = 0
    while pq.qsize() > 0:
        item = pq.get()
        n = cap // item.weight
        maxV += n * item.value
        cap  -= n * item.weight

    return maxV


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
