'''
给定线性序集合中n个元素和一个整数j,1<=j<=n,要求找出这n个元素中第j小的元素
'''



def partition(L, left, right):
    i = left + 1
    j = right
    # 基准元素
    anchor = L[left]
    while i <= j:
        while i <= right and L[i] <= anchor:
            i += 1
        while L[j] > anchor:
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
            i += 1
            j -= 1

    L[left], L[j] = L[j], L[left]
    return j


def randomizedSelect(A, left, right, j):
    if left == right:
        print("left == right")
        return A[left]
    k = partition(A, left, right)
    jNew = k - left + 1
    if j < jNew:
        return randomizedSelect(A, left, k-1, j)
    if j == jNew:
        return A[k]
    else:
        return randomizedSelect(A, k+1, right, j-jNew)


A = [65, 70, 75, 80, 85, 60, 55, 50, 45]
j = 7


print(sorted(A))
print(A)

for j in range(1,8):
    k = randomizedSelect(A, 0, len(A) -1, j)
    print(j, k)

