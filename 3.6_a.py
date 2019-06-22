'''
逆序对问题
A[1,...,n]是一个包含n个不同非负整数的数组。
如果在i<j的情况下，有A[i]>A[j],则(A[i],A[j])就称为A中的一个逆序对。
例如：数组 (3, 1, 4, 5, 2)的逆序对有 (3,1), (3,2), (4,2), (5,2)共4个
枚举方法O(n^2)
用分治策略方法求解O(n*log(n))
'''

def mergeReverse(L1, L2):
    length1 = len(L1)
    length2 = len(L2)
    i , j = 0,0
    crossPairs = 0
    newL = []
    while (i < length1) and (j < length2):
        if L1[i] <= L2[j]:
            newL.append(L1[i])
            i += 1
        else:
            newL.append(L2[j])
            crossPairs += length1 - i
            j += 1

    if i < length1:
        for ii in range(i, length1):
            newL.append(L1[ii])
    else:
        for jj in range(j, length2):
            newL.append(L2[jj])

    print (L1, L2, newL, crossPairs)
    return (crossPairs, newL)


def reverseOrderPairs(L):
    length = len(L)
    if length > 1:
        mid = length // 2

        C1, L1 = reverseOrderPairs(L[:mid])
        C2, L2 = reverseOrderPairs(L[mid:])

        C3, L3 = mergeReverse(L1, L2)

        return (C1 + C2 + C3 , L3)
    else:
        return (0, L)


s = [49, 38, 65, 97, 76, 13, 27]
n, _ = reverseOrderPairs(s)
print(n)