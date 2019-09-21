'''
装载问题
'''

globalC1, C2 = 50, 50
globalWeight = [10, 40, 40]
globalNum    = len(globalWeight)

globalX     = [0] * globalNum
globalBd    = 0
globalWt    = 0
globalMaxWt = 0

def loadingBacktrack(t):
    # 这里需要用global,和作用域范围有关
    global globalMaxWt, globalWt, globalBd

    # print(t)
    # for i in range(t):
    #     print("i = ", i, globalX[i])

    if t == globalNum:
        globalMaxWt = globalWt
        print(globalX, globalMaxWt)
    else:
        globalBd -= globalWeight[t]

        if globalWt + globalWeight[t] <= globalC1:
            globalX[t] = 1
            globalWt += globalWeight[t]
            loadingBacktrack(t+1)
            globalWt -= globalWeight[t]

        if globalWt + globalBd > globalMaxWt:
            globalX[t] = 0
            loadingBacktrack(t+1)

        globalBd += globalWeight[t]

# 开始
totalWeight = 0
for i in range(globalNum):
    totalWeight += globalWeight[i]
globalBd = totalWeight

loadingBacktrack(0)

if totalWeight - globalMaxWt <= C2:
    print(globalMaxWt)
else:
    print("NO")
