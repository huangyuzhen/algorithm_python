'''
数组配对
优化
分桶
'''

A = list(range(1000))
k = 6
n = len(A)

iCount = 0

# 分组
B = [0] * k

for number in A:
    i = number % k
    B[i] += 1

iCount = 0
for i in range(k):
    j = (k - i) % k
    if j < i:
        break
    if j == i:
        iCount += B[i] * (B[i] -1) // 2
    else:
        iCount += B[i] * B[j]

print(iCount)

'''
复杂度 O(k)
'''
