'''
查找问题
给定长度为n的单调不下降数列{a0, a1, ..., a(n-1)}和目标数k
求满足条件 a(i) >= k的最小值i. 不存在是输出n
'''

a = [2,3,3,5,6]
n = len(a)
k = 4

answer = -1
for i in range(n):
    if a[i] >= k:
        answer = i
        break
else:
    answer = n

print(answer)

'''
复杂度 O(n)
'''
