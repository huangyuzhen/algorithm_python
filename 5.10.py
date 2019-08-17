'''
最小生成树
Minimun Cost Tree
Prim算法
'''

INF = 999999

def prim(linkMatrix):
    numV = len(linkMatrix)

    # 1.
    visited = [0] * numV
    lowCost = [INF] * numV
    closest = [-1] * numV

    # 2.
    visited[0] = 1   # 顶点加入MST
    closest[0] = -1  # 树根标记-1
    lowCost[0] = 0
    for i in range(1, numV):
        lowCost[i] = linkMatrix[0][i]
        closest[i] = 0

    costMST = 0

    # 3.
    for _ in range(numV-1):
        mim = INF
        selectV = 0

        for k in range(numV):
            if visited[k] == 0 and lowCost[k] < mim:
                mim = lowCost[k]
                selectV = k

        costMST += mim
        visited[selectV] = 1
        for k in range(numV):
            if visited[k] == 0 and linkMatrix[selectV][k] < lowCost[k]:
                lowCost[k] = linkMatrix[selectV][k]
                closest[k] = selectV

    print(closest)
    print(lowCost)

    return costMST



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


costMST = prim(linkMatrix)
print(costMST)