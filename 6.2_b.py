'''
深度优先搜索
递归方法
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

def dfs(V, node, visited):
    print("visit:", node)
    visited.append(node)

    sonNodes = V.get(node)
    if not sonNodes:
        return

    for son in sonNodes:
        if son not in visited:
            dfs(V, son, visited)

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

print(DFS(V))
