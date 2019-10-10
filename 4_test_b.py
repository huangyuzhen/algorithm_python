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
        dp[(i, 0)] = i
    for j in range(n+1):
        dp[(0, j)] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            key = (i, j)

            if S[i-1] == T[j-1]:
                dp[key] = dp[(i-1, j-1)]
            else:
                a1 = dp[(i-1, j-1)] +1  # replace
                a2 = dp[(i-1, j)] +1    # remove
                a3 = dp[(i, j-1)] +1    # insert
                dp[key] = min(a1, a2, a3)

    return dp[(m,n)]


S = input("")
T = input("")

dis = editDist(S, T)
print(dis)
