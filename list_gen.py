from random import randint

L = []
for i in range(1000):
    n = randint(0, 10000)
    L.append(n)

# print(L)

with open("data.txt", "w") as f:
    for i in L:
        f.write(str(i) + "\n")

# with open("data.txt", "r") as f:
#     lines = f.readlines()
#     datas = list(map(int, lines))
#     print(datas)
