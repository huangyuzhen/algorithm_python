'''
装载问题
'''

globalC1, C2 = 50, 50
globalWeight = [10, 40, 40]
globalNum    = len(globalWeight)

globalX     = [0] * globalNum
globalMaxWt = 0

def loadingBacktrack(t, currentWeight, leftWeight):
    # 这里需要用global,和作用域范围有关
    global globalMaxWt

    if t == globalNum:
        globalMaxWt = currentWeight
        print(globalX, globalMaxWt)
    else:
        leftWeight -= globalWeight[t]

        if currentWeight + globalWeight[t] <= globalC1:
            globalX[t] = 1
            loadingBacktrack(t+1, currentWeight + globalWeight[t], leftWeight)

        if currentWeight + leftWeight > globalMaxWt:
            globalX[t] = 0
            loadingBacktrack(t+1, currentWeight, leftWeight)

# 开始
totalWeight = 0
for i in range(globalNum):
    totalWeight += globalWeight[i]

loadingBacktrack(0, 0, totalWeight)

if totalWeight - globalMaxWt <= C2:
    print(globalMaxWt)
else:
    print("NO")
