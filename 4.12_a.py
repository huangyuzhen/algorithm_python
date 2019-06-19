'''
最大上升子序列
自底向上
O(n^2)
'''

S = [1, 3, 4, 2, 7, 9, 6, 8]

Len = {}
for n in range(1, len(S)+1):
    s = S[n-1]
    maxV = 0
    if n == 1:
        maxV = 1
    else:
        for i in range(1, n):
            t = S[i-1]
            if s > t:
                dis = Len[i] + 1
                if dis > maxV:
                    maxV = dis

    Len[n] = maxV
    print(n, S[n-1], maxV)
