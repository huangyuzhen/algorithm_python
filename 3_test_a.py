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
            # (i,j)位置的数字比x大,(i,j)所在的行,右边的数都比x大，排除此行右边的所有数字
            i += 1
        else:
            # (i,j)位置的数字比x小,(i,j)所在的列,下边的数都比x小，排除此列下边的所有数字
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
