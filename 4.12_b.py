'''
最大上升子序列
自底向上
通过最大限界上升子序列得到最大上升子序列
状态转移方程
Len(m):
m=1: 1
m>1: max{1, (Len(i)+1|1<=i<m,Sm > Si)}
O(n^2)
'''

def lisLength(S):
    maxN = len(S)
    Len = [0] * maxN
    result = 0

    for m in range(maxN):
        Len[m] = 1
        for i in range(m):
            if S[i] < S[m] and Len[i] + 1 > Len[m]:
                Len[m] = Len[i] + 1

        if result < Len[m]:
            result = Len[m]

    return result

S = [1, 3, 4, 2, 7, 9, 6, 8]
maxL = lisLength(S)
print(maxL)
