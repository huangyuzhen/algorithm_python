'''
最小生成树
Minimun Spinning Tree
Kruskal算法
'''

class DisjointSet(dict):
    '''不相交集'''

    def __init__(self, nodes):
        for item in nodes:
            self[item] = item
        pass

    # def add(self, item):
    #     self[item] = item

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

    edges.sort(key = lambda e: e[1])
    # same as above
    # edges = sorted(edges, key=lambda element: element[1])

    totalCost = 0
    cntE = 0
    numV = len(nodes)-1  # 最小生成树的边数等于顶点数减一

    for e in edges:
        x, y = e[0][0], e[0][1]
        fatherX = forest.find(x)
        fatherY = forest.find(y)
        if fatherX != fatherY:
            MST.append(e)
            forest.unionset(fatherX, fatherY)

            totalCost += e[1]
            cntE +=1

            if cntE == numV:
                break

    print(MST)
    return totalCost

def main():
    nodes = 'ABCDEFG'
    edges = [("AB", 7), ("AD", 5),
             ("BC", 8), ("BD", 9), ("BE", 7),
             ("CE", 5),
             ("DE", 15), ("DF", 6),
             ("EF", 8), ("EG", 9),
             ("FG", 11)]

    print(Kruskal(nodes, edges))

if __name__ == '__main__':
    main()
