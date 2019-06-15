
def matrixSearch(A, iLow, iHigh, jLeft, jRight, x):
    if iLow > iHigh or jLeft > jRight:
        return None

    iMid = (iLow + iHigh) // 2
    jMid = (jLeft + jRight) // 2
    current = A[iMid][jMid]

    if current == x:
        return (iMid, jMid)
    elif current > x:
        C = matrixSearch(A, iMid+1, iHigh, jMid, jRight, x)
        return C or matrixSearch(A, iLow, iHigh , jLeft, jMid-1 , x)
    else:
        C = matrixSearch(A, iMid, iHigh, jMid+1, jRight, x)
        return C or matrixSearch(A, iLow, iMid-1, jLeft, jRight, x)

    return None


def search(A, k):
    iSize = len(A)
    if iSize > 0:
        jSize = len(A[0])
        if jSize > 0:
            return matrixSearch(A, 0, iSize-1, 0, jSize-1, k)
    else:
        return None

A = [
    [7, 8, 9],
    [3, 4, 6],
    [1, 2, 5]
]

k = 5
a = search(A, k)
if a:
    print(k, a)
else:
    print(k, "not found")
