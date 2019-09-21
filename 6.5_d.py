'''
装载问题
'''

globalC1, C2 = 50, 50
globalWeight = [10, 40, 40]
globalNum    = len(globalWeight)

globalX     = [0] * globalNum
globalAns   = 0

def loadingBacktrack(t, currentWeight):
    # 这里需要用global,和作用域范围有关
    global globalAns

    if t == globalNum:
        globalAns = currentWeight
        print(globalX, globalAns)
    else:
        if currentWeight + globalWeight[t] <= globalC1:
            globalX[t] = 1
            loadingBacktrack(t+1, currentWeight + globalWeight[t])

        leftWeight = 0
        for i in range(t+1, globalNum):
            leftWeight += globalWeight[i]
        if currentWeight + leftWeight > globalAns:
            globalX[t] = 0
            loadingBacktrack(t+1, currentWeight)

# 开始
totalWeight = 0
for i in range(globalNum):
    totalWeight += globalWeight[i]

loadingBacktrack(0, 0)

if totalWeight - globalAns <= C2:
    print(globalAns)
else:
    print("NO")
