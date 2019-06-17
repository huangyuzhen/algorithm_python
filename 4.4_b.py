'''
矩阵连乘
递归方法，动态规划
备忘录方法
'''

def showSize(P):
    A = {}
    for i in range(1, len(P)):
        A[i] = (P[i-1], P[i])
        print("A{} {}".format(i, A[i]))

P = (30, 35, 15, 5, 10, 20, 25)
memoryTable = {} #备忘录

def matrixChain(i, j):
    key = (i,j)
    if memoryTable.get(key):
        return memoryTable.get(key)

    if i == j:
        memoryTable[key] = 0
        return 0

    minV = 1000000000
    for k in range(i,j):
        answer = matrixChain(i,k)
        answer+= matrixChain(k+1, j)
        answer+= P[i-1] * P[k] * P[j]
        if answer < minV:
            minV = answer

    memoryTable[key] = minV
    #print((i,j), minV)
    return minV


matrixNum = len(P)
m = matrixChain(1, matrixNum - 1)
print(m)

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
