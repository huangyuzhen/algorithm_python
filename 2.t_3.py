
S = ''
for i in range(0,10000):
    S += str(i)

# print(S)

while True:
    t = input("input number: ")
    if t == '':
        break

    l = len(t)
    for i in range(len(S)):
        if t == S[i:i+l]:
            print(i)
            break