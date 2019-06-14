'''
分治法
快速排序
O(n*log(n)) 到 O(n^2), 与划分的k取值有关
可以加入随机取k的方法
'''

def partition(L, left, right):
    i = left + 1
    j = right
    # 基准元素
    anchor = L[left]
    while i <= j:
        while L[i] <= anchor and i <= right:
            i += 1
        while L[j] > anchor:
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
            i += 1
            j -= 1

    L[left], L[j] = L[j], L[left]
    return j

def quickSort(L, left, right):
    if right > left:
        k = partition(L, left, right)
        quickSort(L, left, k-1)
        quickSort(L, k+1, right)


L = [49, 38, 65, 97, 76, 13, 27]
quickSort(L, 0, len(L) -1)

print(L)