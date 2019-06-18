'''
最长子序列问题
递归方法
'''

memoryTable = {} #备忘录

def maxSubStringRecursive(X, Y, i, j):
    if i == 0 or j == 0:
        return 0

    key = (i,j)
    if memoryTable.get(key):
        return memoryTable.get(key)

    if X[i-1] == Y[j-1]:
        maxV = maxSubStringRecursive(X, Y, i-1, j-1) + 1
    else:
        a1 = maxSubStringRecursive(X, Y, i, j-1)
        a2 = maxSubStringRecursive(X, Y, i-1, j)
        maxV = max(a1, a2)

    memoryTable[key] = maxV
    return maxV

def maxSubString(X, Y):
    m = len(X)
    n = len(Y)
    return maxSubStringRecursive(X, Y, m, n)


X = input("input string 1: ")
Y = input("input string 2: ")

d = maxSubString(X, Y)
print(d)
