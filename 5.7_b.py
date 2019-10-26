'''
单源最短路径
复杂度 O(N^2)
Dijkstra算法
'''

INFINITY = 999999

def Dijkstra(linkMatrix, nodeList, beginV):
    numV = len(nodeList)
    preV = {beginV: -1}

    visited = {}
    lowLR   = {}
    for node in nodeList:
        visited[node] = 0
        lowLR[node]   = INFINITY

    # 开始节点
    lowLR[beginV]   = 0
    visited[beginV] = 1

    selectV = beginV
    for _ in range(numV-1):
        cost = linkMatrix.get(selectV)
        for node in nodeList:
            if visited[node] == 0 and cost.get(node):
                newCost = lowLR[selectV] + cost[node]
                if newCost < lowLR[node]:
                    lowLR[node] = newCost
                    preV[node]  = selectV

        minmal = INFINITY
        for node in nodeList:
            if visited[node] == 0 and lowLR[node] < minmal:
                minmal = lowLR[node]
                selectV = node

        visited[selectV] = 1
        # print(lowLR)


    return lowLR, preV

cost = {
    'A': {'C': 2, 'D': 6, 'B': 9},
    'B': {'E': 4},
    'C': {'F': 1, 'D': 3},
    'D': {'B': 2, 'E': 7, 'G': 9},
    'E': {'G': 1, 'H': 5},
    'F': {'D': 1, 'I': 6},
    'G': {'I': 5, 'H': 1},
    'H': {},
    'I': {'H': 5}
 }

nodeList = ''.join(cost.keys())
ans, preV = Dijkstra(cost, nodeList, 'A')

for k in ans:
    print(k, ans[k])

print(preV)
