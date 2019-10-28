'''
单源最短路径
负责度 O(N^2)
Dijkstra算法
'''

INF = 999

def Dijkstra(linkMatrix, beginV = 0):
    numV = len(linkMatrix)

    # 1.
    visited = [0]   * numV
    lowCost = [INF] * numV
    closest = [-1]  * numV

    # 2.
    selectV = beginV
    visited[selectV] = 1
    closest[selectV] = -1
    lowCost[selectV] = 0

    for _ in range(numV-1):
        for k in range(numV):
            newCost = lowCost[selectV] + linkMatrix[selectV][k]
            if visited[k] == 0 and newCost < lowCost[k]:
                lowCost[k] = newCost
                closest[k] = selectV

        mim = INF
        for k in range(numV):
            if visited[k] == 0 and lowCost[k] < mim:
                mim = lowCost[k]
                selectV = k

        visited[selectV] = 1

    print(closest)
    return lowCost


linkMatrix = [
    [INF, 10, INF, 30, 100],
    [INF, INF, 50, INF, INF],
    [INF, INF, INF, INF, 10],
    [INF, INF, 20, INF, 60],
    [INF, INF, INF, INF, INF]
]



cost = Dijkstra(linkMatrix, 0)
print(cost)
