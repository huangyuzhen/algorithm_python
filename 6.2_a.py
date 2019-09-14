'''
深度优先搜索
后进先出的 LIFO stack
'''

# 邻接表
V = {
    "A": ["F", "G"],
    "B": ["A", "I"],
    "C": ["A", "D"],
    "D": ["C", "F"],
    "E": ["C", "D", "G"],
    "F": ["E"],
    "G": [],
    "H": "B",
    "I": "H",
}

def dfs(V, initNode, visited):
    stack = [initNode]

    while True:
        if len(stack) <= 0:
            return

        node = stack.pop()
        if node in visited:
            # print("visited:", node)
            continue

        print("visit:", node)
        visited.append(node)

        sonNodes = V.get(node)
        if sonNodes:
            for son in sonNodes[::-1]:
                if son not in visited:
                    stack.append(son)
                else:
                    # 已经访问过
                    # print("skip", node + son)
                    pass
        else:
            # 此node无子节点
            pass


def DFS(V):
    Visited = []

    while True:
        if len(Visited) >= len(V):
            break

        for k in V.keys():
            if k not in Visited:
                initNode = k
                break

        dfs(V, initNode, Visited)

    return Visited

DFS(V)
