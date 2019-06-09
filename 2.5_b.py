'''
查找问题优化
二分查找
'''

a = [2,3,3,3,3,3,3,3,3,3,3,3,5,6]
n = len(a)
k = 4


lb = 0
ub = n

while lb < ub:
    mid = int((lb + ub) // 2)
    if a[mid] >= k:
        ub = mid
    else:
        lb = mid + 1

if lb < n:
    print("found", lb)
else:
    print("not found", lb)

'''
复杂度 O(log(n))
'''