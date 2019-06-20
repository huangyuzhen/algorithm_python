'''
收集控的决策问题
递归算法,有备忘录
'''

memoryTable = {} #备忘录

def P(weight, value, capacity):
    maxV = memoryTable.get(capacity, -1)
    if maxV >= 0:
        return maxV

    maxV = 0
    for i in range(len(weight)):
        w = weight[i]
        if capacity >= w:
            m = P(weight, value, capacity - w) + value[i]
            if m > maxV:
                maxV = m

    memoryTable[capacity] = maxV
    return maxV



n = int(input(""))

for i in range(n):
    line2 = input("").split()
    num = int(line2[0])
    capacity = int(line2[1])

    value = []
    weight = []

    line3 = input("").split()
    line4 = input("").split()
    for i in range(num):
        value.append(int(line3[i]))
        weight.append(int(line4[i]))

    maxValue = P(weight, value, capacity)
    print("result:",maxValue)
