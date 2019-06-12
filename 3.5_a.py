'''
分治
合并排序
'''

def merge(L1, L2):
    length1 = len(L1)
    length2 = len(L2)
    i , j = 0,0
    result = []
    while (i < length1) and (j < length2):
        if L1[i] <= L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1

    if i < length1:
        for ii in range(i, length1):
            result.append(L1[ii])
    else:
        for jj in range(j, length2):
            result.append(L2[jj])

    return result

def mergeSort(L):
    length = len(L)
    if length > 1:
        mid = length // 2
        L1 = mergeSort(L[:mid])
        L2 = mergeSort(L[mid:])

        R = merge(L1, L2)
    else:
        R = L
    return R


b = [ 4, 1, 8, 6, 11, 10, 12]
s = mergeSort(b)
print(s)

'''
算法复杂度
O(nlog(n))
'''
