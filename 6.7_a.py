'''
装载问题
集装箱装载问题
BFS算法
'''

globalC1, C2 = 50, 50
globalWeight = [10, 40, 40]
globalNum    = len(globalWeight)

WEIGHT = 0
INDEX  = 1

def loadingBFS():
    maxWt = 0
    headNode = [0, -1]
    queue = [headNode]

    while True:
        if len(queue) <= 0:
            return maxWt

        node = queue[0]
        queue = queue[1:]

        if node[INDEX] + 1 >= globalNum:
            # print(node)
            if node[WEIGHT] <= globalC1 and node[WEIGHT] > maxWt:
                maxWt = node[WEIGHT]
        else:
            # 扩展子节点
            index   = node[INDEX] + 1
            weight  = node[WEIGHT]
            current = globalWeight[index]

            # 当前物品装入,左自节点
            queue.append([weight + current, index])

            # 当前物品不装,右自节点
            queue.append([weight, index])

    return maxWt


maxWeight = loadingBFS()

totalWeight = 0
for i in range(globalNum):
    totalWeight += globalWeight[i]

if totalWeight - maxWeight <= C2:
    print(maxWeight)
else:
    print("NO")
