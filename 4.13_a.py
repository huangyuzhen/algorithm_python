'''
最大上升子序列
O(n^2)
'''

S = [1, 13, 14, 2, 19, 16, 18, 3, 5, 7, 9, 11]

Len = 0
n = len(S)
T = [0] * (n + 1)

for i in range(1, n+1):
    s = S[i-1]
    if s > T[Len]:
        Len += 1
        T[Len] = s
    else:
        for j in range(1,Len+1):
            if s < T[j]:
                T[j] = s
                break

print(Len)

'''
第二层循环可以用二分查找优化
'''