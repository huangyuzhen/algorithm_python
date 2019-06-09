'''
递归方法构造
二叉树
'''


globalNum  = 10
globalFlag = list(range(globalNum))

s = set()

def recursiveEnum(t):
    if t == globalNum:
        s.add(tuple(globalFlag))

    else:
        globalFlag[t] = 0
        recursiveEnum(t+1)
        globalFlag[t] = 1
        recursiveEnum(t+1)

recursiveEnum(0)

print(len(s))
