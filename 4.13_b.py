'''
最大上升子序列
第二层循环用二分查找优化
复杂度: O(n*log(n))
'''

S = [1, 13, 14, 2, 19, 16, 18, 2, 3, 5, 7, 9, 11]
# S = [1, 13, 14, 2, 19, 16, 18]

Len = 0
n = len(S)
T = [0] + [-1] * (n + 1)

for i in range(1, n+1):
    s = S[i-1]
    if s > T[Len]:
        Len += 1
        T[Len] = s
    else:
        # 用二分查找
        lb = 0
        ub = Len
        while lb < ub:
            mid = int((lb + ub) // 2)
            if T[mid] < s:
                lb = mid + 1
            else:
                ub = mid
        if lb <= Len:
            T[lb] = s

print(Len)
print(T)
