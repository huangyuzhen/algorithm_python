'''
矩阵连乘
'''

P = (30, 35, 15, 5, 10, 20, 25)


def showSize(P):
    A = {}
    for i in range(1, len(P)):
        A[i] = (P[i-1], P[i])
        print("A{} {}".format(i, A[i]))


matrixNum = len(P)

memoryTable = {}
bestK = {}
for i in range(1, matrixNum):
    memoryTable[(i, i)] = 0
    bestK[(i,i)] = i

for length in range(2, matrixNum):
    for i in range(1, matrixNum - length + 1):
        j = i + length - 1
        key = (i,j)
        memoryTable[key] = 100000000
        for k in range(i, j):
            ans = memoryTable[(i,k)]
            ans+= memoryTable[(k+1,j)]
            ans+= P[i-1] * P[k] * P[j]
            if ans < memoryTable[key]:
                memoryTable[key] = ans
                bestK[key] = k


print("memoryTable:")
print(" ", end='')
for i in range(1, matrixNum):
    print("{:10d}".format(i), end = '')
print()
for i in range(1, matrixNum):
    print(i, end='')
    for j in range(1, matrixNum):
        key = (i,j)
        if i>j:
            print(" "*10, end = '')
        else:
            print("{:10d}".format(memoryTable[key]), end = '')
    print()


print(bestK)