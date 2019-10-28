'''
最小生成树
Minimun Cost Tree
Prim算法
'''

INF = 999

def prim(linkMatrix, beginV = 0):
    numV = len(linkMatrix)

    # 1.
    visited = [0] * numV
    lowCost = [INF] * numV
    closest = [-1] * numV

    # 2. beginV起始点
    selectV = beginV
    visited[selectV] = 1
    closest[selectV] = -1
    lowCost[selectV] = 0

    # 3.
    for _ in range(numV-1):
        for k in range(numV):
            if visited[k] == 0 and linkMatrix[selectV][k] < lowCost[k]:
                lowCost[k] = linkMatrix[selectV][k]
                closest[k] = selectV

        mim = INF
        for k in range(numV):
            if visited[k] == 0 and lowCost[k] < mim:
                mim = lowCost[k]
                selectV = k

        visited[selectV] = 1

    print(closest)
    print(lowCost)
    return sum(lowCost)


'''
带权无向图，用链接矩阵表示
'''
linkMatrix = [
    [0, 2, 2, 1, INF, INF, INF],
    [2, 0, INF, 5, 1, INF, INF],
    [2, INF, 0, 1, INF, 2, INF],
    [1, 5, 1, 0, 1, 6, 5],
    [INF, 1, INF, 1, 0, INF, 3],
    [INF, INF, 2, 6, INF, 0, 10],
    [INF, INF, INF, 5, 3, 10, 0],
]

for i in range(len(linkMatrix)):
    costMST = prim(linkMatrix, i)
    print(costMST)
