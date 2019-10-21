'''
最大上升子序列
T[k] 存储所有Len[i] = k 中最小的S[i]
O(n^2)
'''

S = [1, 3, 4, 2, 9, 6, 8]

Len = 0
n = len(S)
T = [0] * (n + 1)

for i in range(n):
    s = S[i]
    if s > T[Len]:
        T[Len+1] = s
        Len += 1
    else:
        for j in range(1,Len+1):
            if s <= T[j]:
                T[j] = s
                break
    print(Len, T)

'''
第二层循环可以用二分查找优化
'''