'''
绳子切割 优化
二分枚举
'''


L = [8.02, 7.43, 4.57, 5.39]
N = len(L)
K = 11


lb = 0
ub = 100000

while lb < ub:
    mid = int((lb + ub)//2)
    if mid == lb:    # 除法会向下取
        mid += 1

    length = 0.01 * mid

    k = 0
    for l in L:
        k += int(l / length)

    if k >= K:
        lb = mid
    else:
        ub = mid - 1

print(lb, lb * 0.01)

'''
复杂度 O(log(n))
'''
