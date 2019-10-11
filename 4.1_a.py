'''
数字三角型，路径问题
给定等腰直角数字三角形,从顶到底的某个位置的一条路径，使该路径所经过的数字的总和最大，假设每一步可以延直线向下或者右斜线向下走
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''

A = [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5]
]

step = []
opt = []
for a in A:
    l = [0] * len(a)
    opt.append(l)
    step.append(l[:])


for j in range(5):
    for i in range(j, 5):
        if j == 0:
            if i == 0:
                opt[i][0] = A[i][0]
            else:
                opt[i][0] = A[i][0] + opt[i-1][0]
            step[i][0] = 1
        else:
            a = -1
            if i-1 >= j:
                a = opt[i-1][j]
            b = opt[i-1][j-1]
            if a > b:
                step[i][j] = 1
            else:
                step[i][j] = 2
            opt[i][j] = A[i][j] + max(a,b)



for o in opt:
    print(o)

for s in step:
    print(s)