'''
装载问题
启发式搜索
评估函数，优先队列
'''
from queue import PriorityQueue as PQueue

class CompareAble:
    def __init__(self, weight = 0, bd = 0, idx = 0):
        self.Wt = weight
        self.Bd = bd
        self.idx = idx

    # 这里是按python3语法，定义的 < 方法
    def __lt__(self, other):
        if self.Wt + self.Bd < other.Wt + other.Bd:
            return False
        else:
            return True


def loadingHeuristic():
    headNode = CompareAble(0, sum(globalWeight), -1)
    queue = PQueue()
    queue.put(headNode)

    while queue.qsize() > 0:
        headNode = queue.get()
        print("get:  ", headNode.Wt, headNode.Bd, headNode.idx)

        if headNode.idx + 1 >= globalNum:
            return headNode.Wt
        else:
            current = globalWeight[headNode.idx + 1]

            # 扩展左子节点
            son = CompareAble(headNode.Wt + current, headNode.Bd - current, headNode.idx + 1)
            if son.Wt <= globalC1:
                queue.put(son)
                # print("left: ", son.Wt, son.Bd, son.idx)

            #扩展右子节点
            son = CompareAble(headNode.Wt, headNode.Bd - current, headNode.idx + 1)
            queue.put(son)
            # print("right:", son.Wt, son.Bd, son.idx)

    return -1


globalC1, C2 = 50, 50
globalWeight = [10, 40, 40]
globalNum    = len(globalWeight)

maxWeight = loadingHeuristic()

if sum(globalWeight) - maxWeight <= C2:
    print(maxWeight)
else:
    print("NO")