'''
0-1背包问题
递归算法
'''

memoryTable = {} #备忘录
def ValueDp(weight, value, i, p):
    if i == 0 or p == 0:
        return 0

    key = (i, p)
    if memoryTable.get(key):
        return memoryTable.get(key)
    # print(i,p)

    w = weight[i-1]
    v = value[i-1]

    if w > p:
        maxV = ValueDp(weight, value, i-1, p)
    else:
        a1 = ValueDp(weight, value, i-1, p)
        a2 = ValueDp(weight, value, i-1, p-w) + v
        maxV = max(a1, a2)

    memoryTable[key] = maxV
    return maxV


weight = [2, 2, 6, 5, 4]
value  = [6, 3, 5, 4, 6]
n = len(weight)
C = 10

maxV = ValueDp(weight, value, n, C)
print(maxV)
