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
    [7            ],
    [3, 8         ],
    [8, 1, 0      ],
    [2, 7, 4, 4   ],
    [4, 5, 2, 6, 5],
]

step = []
opt = []
for a in A:
    l = [0] * len(a)
    opt.append(l)
    step.append(l[:])

# 逐行填充opt
for i in range(5):
    for j in range(i+1):
        if j == 0:
            # 每行左边第一个
            step[i][j] = 1   # 1=直线向下
            if i == 0:
                opt[i][j] = A[i][j]
            else:
                opt[i][j] = A[i][j] + opt[i-1][j]
        elif j == i:
            # 每行最后一个
            step[i][j] = 2   # 2=右斜线向下
            opt[i][j] = A[i][j] + opt[i-1][j-1]
        else:
            a = opt[i-1][j]
            b = opt[i-1][j-1]
            if b > a:
                step[i][j] = 2
                opt[i][j] = A[i][j] + opt[i-1][j-1]
            else:
                step[i][j] = 1
                opt[i][j] = A[i][j] + opt[i-1][j]

    print(opt[i])


for s in step:
    print(s)