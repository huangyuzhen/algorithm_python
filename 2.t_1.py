
def find(N):
    r = []
    for a in range(1, N+1):
        for b in range(1,a):
            for c in range(b,a):
                for d in range(c, a):
                    # print(a, b, c, d)
                    if a*a*a == b*b*b + c*c*c + d*d*d:
                        r.append((a,b,c,d))
    print(r)
    return r

n = int(input("input number(<= 100): "))
r = find(n)
print(len(r))
