'''
二分查找
减治方法
在分治算法中，如果划分的某个子问题可以不用求解，或者与其他自问题有重复（已求解)
则这个自问题不用递归求解，直接舍弃或者取已有结果
'''

def binarySearch(L, k):
    left = 0
    right = len(L) -1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if k == L[mid]:
            return mid
        if k < L[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


L = list(range(100))

k = binarySearch(L, 40)
print(k)