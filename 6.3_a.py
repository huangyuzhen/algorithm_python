'''
广度优先搜索
先进先出的 FIFO queue
'''

# 邻接表
V = {
    "A": ["B", "I"],
    "B": ["A", "F"],
    "C": ["D", "G", "H"],
    "D": ["C"],
    "E": ["F", "I"],
    "F": ["B", "E", "G", "I"],
    "G": ["C", "F", "H"],
    "H": ["C", "G"],
    "I": ["A", "E", "F"],
}

def bfs(V, initNode, visited):
    queue = [initNode]

    while True:
        if len(queue) <= 0:
            return

        node = queue[0]
        queue = queue[1:]
        if node in visited:
            # print("visited:", node)
            continue

        print("visit:", node)
        visited.append(node)

        sonNodes = V.get(node)
        if sonNodes:
            for son in sonNodes:
                if son not in visited:
                    queue.append(son)
                else:
                    # 已经访问过
                    # print("skip", node + son)
                    pass
        else:
            # 此node无子节点
            pass


def BFS(V):
    Visited = []

    while True:
        if len(Visited) >= len(V):
            break

        for k in V.keys():
            if k not in Visited:
                initNode = k
                break

        print("initNode", initNode)
        bfs(V, initNode, Visited)

    return Visited

print(BFS(V))
