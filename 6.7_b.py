'''
装载问题
集装箱装载问题
分支限界减剪枝
'''

globalC1, C2 = 50, 50
globalWeight = [10, 40, 40]
globalNum    = len(globalWeight)

WEIGHT = 0
BD     = 1
INDEX  = 2

def loadingBFS():
    maxWt = 0
    bd = sum(globalWeight) # BD值
    headNode = (0, bd, -1)
    queue = [headNode]

    while True:
        if len(queue) <= 0:
            return maxWt

        node = queue[0]
        queue = queue[1:]

        if node[INDEX] + 1 >= globalNum:
            print(node)
            if node[WEIGHT] <= globalC1 and node[WEIGHT] > maxWt:
                maxWt = node[WEIGHT]
        else:
            # 扩展子节点
            index   = node[INDEX] + 1
            weight  = node[WEIGHT]

            # 左子节点,当前物品装入
            current = globalWeight[index]
            bd = node[BD] - current

            if current+weight <= globalC1:
                print("queue1:", (current+weight, bd, index))
                queue.append((current+weight, bd, index))
                if current+weight > maxWt:
                    maxWt = current+weight

            # 右子节点,当前物品不装入
            if weight + bd > maxWt:
                print("queue2:", (weight, bd, index))
                queue.append((weight, bd, index))

    return maxWt


maxWeight = loadingBFS()

totalWeight = 0
for i in range(globalNum):
    totalWeight += globalWeight[i]

if totalWeight - maxWeight <= C2:
    print(maxWeight)
else:
    print("NO")
