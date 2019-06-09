'''
数组配对
长度为n的数组，和正整数k,问从数组中人选两个数使其和是k的倍数，有多少种选法.
对于数组a1=1, a2=2, a3=2 而言
(a1,a2)和(a2,a1)被认为是同一种选法
(a1,a2)和(a1,a3)被认为是不同的选法
'''

A = list(range(1000))
k = 6
n = len(A)

iCount = 0

for i in range(n):
    for j in range(i+1,n):
        if (A[i] + A[j]) % k == 0:
            iCount +=1
            # print(A[i], A[j])

print(iCount)

'''
复杂度 O(n*n)
'''
