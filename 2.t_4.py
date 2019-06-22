'''
全排列
从n个元素取n个元素全部排列
自底向上生成
'''

S = 'abcdef'
n = len(S)


P = {}
P[0] = ['']
for i in range(1, n+1):
    li = []
    s = S[i-1]
    #把s 与 p[0]组成排列
    for p in P[i-1]:
        n = len(p)
        for k in range(n+1):
            idx = n - k
            newS = p[:idx] + s + p[idx:]
            li.append(newS)
    P[i] = li


for i in range(1, len(S)+1):
    print(i, len(P[i]))
