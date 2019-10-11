'''
矩阵连乘
递归方法，动态规划
备忘录方法
'''

P = (30, 35, 15, 5, 10, 20, 25)
memoryTable = {} #备忘录
bestK = {}

def matrixChain(i, j):
    key = (i,j)
    if i >= j:
        memoryTable[key] = 0
        return 0

    if memoryTable.get(key):
        return memoryTable.get(key)

    minV = 1000000000
    for k in range(i,j):
        answer1 = matrixChain(i,k)
        answer2 = matrixChain(k+1, j)
        answer  = answer1 + answer2 + P[i-1] * P[k] * P[j]
        # print(i,k,j, answer)
        if answer < minV:
            minV = answer
            bestK[key] = k

    memoryTable[key] = minV
    # print(key, minV)
    return minV


matrixNum = len(P)
m = matrixChain(1, matrixNum - 1)
print(m)

# 输出memoryTable
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