#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
matrixSearch O(n)
'''

def matrixSearch(A, x):
    iRight = len(A)
    jRight = len(A[0])

    i, j = 0, 0
    while i < iRight and j < jRight:
        value = A[i][j]
        if value == x:
            return True
        if value > x:
            i += 1
        else:
            j += 1

    return False


A = [
    [7, 8, 9],
    [3, 4, 6],
    [1, 2, 5]
]

x = input("input number: ")
if x != '':
    x = int(x)
    a = matrixSearch(A, x)
    print(a)
