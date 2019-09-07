import time
start = time.perf_counter()
class DisjointSet(dict):
    '''不相交集'''

    def __init__(self, nodes):
        for item in nodes:
            self[item] = item
        pass

    def add(self, item):
        self[item] = item

    def find(self, item):
        if self[item] != item:
            self[item] = self.find(self[item])
        return self[item]

    def unionset(self, item1, item2):
        self[item2] = self[item1]

def Kruskal(nodes, edges):
    '''基于不相交集实现Kruskal算法'''
    forest = DisjointSet(nodes)
    MST = []

    edges.sort(key = lambda e: e[2])
    # same as above
    # edges = sorted(edges, key=lambda element: element[2])

    num_sides = len(nodes)-1  # 最小生成树的边数等于顶点数减一
    for e in edges:
        node1, node2, _ = e
        parent1 = forest.find(node1)
        parent2 = forest.find(node2)
        if parent1 != parent2:
            MST.append(e)
            num_sides -= 1
            if num_sides == 0:
                return MST
            else:
                forest.unionset(parent1, parent2)
    pass

def main():
    nodes = set(list('ABCDEFG'))
    edges = [("A", "B", 7), ("A", "D", 5),
             ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
             ("C", "E", 5),
             ("D", "E", 15), ("D", "F", 6),
             ("E", "F", 8), ("E", "G", 9),
             ("F", "G", 11)]

    print("The undirected graph is :", edges)
    print("\nThe minimum spanning tree by Kruskal is : ")
    print(Kruskal(nodes, edges))

if __name__ == '__main__':
    main()
end = time.perf_counter()   #结束计时
print('Running time: %f seconds'%(end-start))  #程序运行时间
