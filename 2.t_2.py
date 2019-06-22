
A = 3.14159265358979
L = 10000


gap = 99999
for n in range(1, L):
    for d in range(1, L):
        diff =  n / d - A
        if diff < 0:
            diff = -diff
        if diff < gap:
            nd = (n, d)
            print(nd, diff)
            gap = diff

print(nd)
