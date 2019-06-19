'''
0-1背包问题
跳跃点解法
'''

weight = [2, 2, 6, 5, 4]
value  = [6, 3, 5, 4, 6]
n = len(weight)
C = 10


P = {}
P[0] = {(0,0)}

for i in range(1, n+1):
    e = (weight[i-1], value[i-1])
    p = P[i-1]
    # 计算 q[i-1]
    q = []
    for v in p:
        a = v[0] + e[0]
        b = v[1] + e[1]
        if a <= C:
            q.append((a, b))

    # 合并 p[i-1] 和 q[i-1] 得到 p[i]
    P[i] = set()

    for x in q:
        for y in p:
            if x[0] >= y[0] and x[1] < y[1]:
                break
        else:
            P[i].add(x)

    for x in p:
        for y in q:
            if x[0] >= y[0] and x[1] < y[1]:
                break
        else:
            P[i].add(x)

    print(i, sorted(P[i]))
