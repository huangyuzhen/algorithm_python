'''
石头移动问题

有一条河，河中间有一些石头，石头的数量以及相邻两块石头之间的距离已知。现在可以移除一些石头，
假设最多可以移除m块石头，（首尾两块石头不能移除，且假定所有石头都处于同一条直线），
问最多移除m块石头后相邻两块石头之间的最小距离的最大值是多少?
'''


stones = (0, 4, 5, 8, 10)


globalNum = len(stones)-2
globalAns = 0
resultStones = tuple()

stoneFlag = list(range(globalNum))


def checkStone(flag, stones):
    removeCount = 0
    flag.insert(0, 0)
    flag.append(0)

    for b in flag:
        if b == 1:
            removeCount +=1
    if removeCount > 2:
        return 0

    remainStones = []
    for i in range(len(flag)):
        if flag[i] == 0:
            remainStones.append(stones[i])
    dist = remainStones[-1] - remainStones[0]
    for i in range(len(remainStones)-1):
        d = remainStones[i+1] - remainStones[i]
        if d < dist:
            dist = d

    global globalAns,resultStones
    if dist >= globalAns:
        globalAns = dist
        resultStones = tuple(remainStones)
        print(resultStones, dist)

    return dist



def recursiveEnum(t):
    global globalNum
    if t == globalNum:
        # print(globalFlag)
        checkStone(stoneFlag[:], stones)

    else:
        stoneFlag[t] = 0
        recursiveEnum(t+1)
        stoneFlag[t] = 1
        recursiveEnum(t+1)

recursiveEnum(0)

print(resultStones, globalAns)

'''
复杂度 O(2**n)
'''
