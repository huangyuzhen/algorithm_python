'''
装载问题
'''

globalC1, C2 = 50, 50
globalWeight = [10, 40, 40]
globalNum    = len(globalWeight)

globalX   = [0] * globalNum
globalAns = 0

def loadingDFS(t):
    # 这里需要用global,和作用域范围有关
    global globalAns

    if t == globalNum:
        sumWeight = 0
        for i in range(globalNum):
            sumWeight += globalX[i] * globalWeight[i]
        # print(globalX, sumWeight)
        if sumWeight <= globalC1 and sumWeight > globalAns:
            globalAns = sumWeight
        return
    else:
        # 深度优先搜索
        globalX[t] = 1
        loadingDFS(t+1)

        globalX[t] = 0
        loadingDFS(t+1)


totalWeight = 0
for i in range(globalNum):
    totalWeight += globalWeight[i]

loadingDFS(0)

if totalWeight - globalAns <= C2:
    print(globalAns)
else:
    print("NO")
