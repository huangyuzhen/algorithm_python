'''
0-1背包问题
自底向上
'''

weight = [2, 2, 6, 5, 4]
value  = [6, 3, 5, 4, 6]
n = len(weight)
C = 10

# V[(i,p)] 表示背包容量为p时，待考虑物品集{0,1,2,...,i}时的最大装入物品价值
# V[(5,10)] 5个物品，容量10时
# C: capacity

V = {}
for i in range(n+1):
    V[(i,0)] = 0
for p in range(C+1):
    V[(0, p)] = 0

for i in range(1, n+1):
    for p in range(1, C+1):
        key = (i,p)
        w = weight[i-1]
        v = value[i-1]
        if w > p:
            V[key] = V[(i-1, p)]
        else:
            a1 = V[(i-1, p)]
            a2 = V[(i-1, p-w)] + v
            a = max(a1, a2)
            V[key] = a
        print("{:4d}".format(V[key]), end = ' ')
    print()

print(V[(n,C)])

