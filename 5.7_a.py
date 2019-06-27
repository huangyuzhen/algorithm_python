'''
单源最短路径
负责度 O(N^2)
Dijkstra算法
'''

INFINITY = 999999

def Dijkstra(linkMatrix, numV, beginV):
    visited = [0] * numV
    preV = {}
    lowLR = [0] * numV

    visited[beginV] = 1

    for i in range(numV):
        lowLR[i] = linkMatrix[beginV][i]
        preV[i] = beginV

    lowLR[beginV] = 0
    preV[beginV] = -1

    selectV = beginV
    for i in range(1, numV):
        for j in range(numV):
            newCost = lowLR[selectV] + linkMatrix[selectV][j]
            if visited[j] == 0 and newCost < lowLR[j]:
                lowLR[j] = newCost
                preV[j] = selectV

        minmal = INFINITY
        for j in range(numV):
            if visited[j] == 0 and lowLR[j] < minmal:
                minmal = lowLR[j]
                selectV = j

        visited[selectV] = 1


    return lowLR, preV





cost = [
    [INFINITY, 10, INFINITY, 30, 100],
    [INFINITY, INFINITY, 50, INFINITY, INFINITY],
    [INFINITY, INFINITY, INFINITY, INFINITY, 10],
    [INFINITY, INFINITY, 20, INFINITY, 60],
    [INFINITY, INFINITY, INFINITY, INFINITY, INFINITY]
]



n = len(cost)

ans, preV = Dijkstra(cost, n, 0)
print(ans)
print(preV)
