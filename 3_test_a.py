
def matrixSearch(A, x):
    iRight = len(A)
    jRight = len(A[0])

    i, j = 0, 0
    while i < iRight and j < jRight:
        value = A[i][j]
        if value == x:
            return (i, j)
        if value > x:
            i += 1
        else:
            j += 1


    return None

A = [
    [7, 8, 9, ],
    [3, 4, 6, ],
    [1, 2, 5, ]
]


for i in range(10):
    print("check", i)
    a = matrixSearch(A, i)
    if a:
       print(a)
    else:
       print("not found")

