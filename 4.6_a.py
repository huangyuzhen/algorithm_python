'''
多段图问题
'''

V = [
    [0],
    [0, 1],
    [0, 2, 3, 4, 5],
    [0, 6, 7, 8],
    [0, 9, 10, 11],
    [0, 12]
]

Weight = {
    (1,2): 9, (1,3): 7, (1,4): 3, (1,5): 2,
    (2,6): 4, (2,7): 2, (2,8): 1,
    (3,6): 2, (3,7): 7,
    (4,8): 11,
    (5,7): 11, (5,8): 8,
    (6,9): 6, (6,10): 5,
    (7,9): 4, (7,10): 3,
    (8,10): 5, (8,11): 6,
    (9,12): 4, (10,12): 2, (11,12):5
}


W = {}
for i in range(1, len(V)):
    for p in range(1, len(V[i])):
        key = (i, p)
        if i == 1:
            W[key] = 0
            continue

        dis = 999999
        for q in range(1, len(V[i-1])):
            a1 = W.get((i-1, q), -1)
            if a1 < 0:
                continue

            kk = (V[i-1][q], V[i][p])
            a2 = Weight.get(kk, -1)
            if a2 < 0:
                continue

            a = a1 + a2
            if a < dis:
                dis = a

        W[key] = dis
        print("point:", V[i][p], key, dis)


print(W)
