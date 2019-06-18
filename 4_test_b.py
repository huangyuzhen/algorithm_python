#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
最小编辑距离
自底向上
'''

def editDist(S, T):
    m = len(S)
    n = len(T)

    dp = {}
    for i in range(m+1):
        for j in range(n+1):
            key = (i, j)
            if i == 0 or j == 0:
                dp[key] = i + j
                continue

            if S[i-1] == T[j-1]:
                dp[key] = dp[(i-1, j-1)]
            else:
                a1 = dp[(i-1, j-1)]    # replace
                a2 = dp[(i-1, j)]      # remove
                a3 = dp[(i, j-1)]      # insert
                dp[key] = min(a1, a2, a3) + 1

    return dp


S = input("input string 1: ")
T = input("input string 2: ")

dp = editDist(S, T)
dis = dp[(len(S), len(T))]
print(dis)
