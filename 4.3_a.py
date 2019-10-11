'''
矩阵连乘
'''

P = (30, 35, 15, 5, 10, 20, 25)
matrixNum = len(P)

memoryTable = {}
bestK = {}

for i in range(1, matrixNum):
    memoryTable[(i, i)] = 0

for length in range(1, matrixNum):
    for i in range(1, matrixNum - length):
        j = i + length
        key = (i,j)
        memoryTable[key] = 100000000
        for k in range(i, j):
            ans1 = memoryTable[(i,k)]
            ans2 = memoryTable[(k+1,j)]
            ans  = ans1 + ans2 + P[i-1] * P[k] * P[j]
            if ans < memoryTable[key]:
                memoryTable[key] = ans
                bestK[key] = k

print(memoryTable[(1,matrixNum-1)])

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