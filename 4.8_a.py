'''
最长子序列问题
自底向上，递推方法求解
'''


def maxSubString(X, Y):
    m = len(X)
    n = len(Y)

    C = {}
    B = {}

    for i in range(m+1):
        C[(i,0)] = 0
    for j in range(n+1):
        C[(0,j)] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            key = (i,j)

            x = X[i-1]
            y = Y[j-1]
            if x == y:
                C[key] = C[(i-1, j-1)] + 1
                B[key] = 1
            else:
                # <= 或者用 < 都可以,但是构造出来的子串不同
                if C[(i, j-1)] <= C[(i-1, j)]:
                    C[key] = C[(i-1, j)]
                    B[key] = 2
                else:
                    C[key] = C[(i, j-1)]
                    B[key] = 3

    '''
    取得公共串
    '''
    s = ''
    i, j = len(X), len(Y)
    while i > 0 and j>0:
        b = B[(i,j)]
        if b == 1:
            s += X[i-1]
            i -= 1
            j -= 1
        elif b == 2:
            i -= 1
        else:
            j -= 1

    return C[(m,n)], s[::-1]


# X = input("input string 1: ")
# Y = input("input string 2: ")

X = "ABCBDAB"
Y = "BDCABA"

d, s = maxSubString(X, Y)
print(d,s)
