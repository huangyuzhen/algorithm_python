'''
线性时间选择
'''


with open("data.txt", "r") as f:
    lines = f.readlines()
    datas = list(map(int, lines))
    # print(datas)

# print(len(datas))


def median(L):
    '''
    use bubble sort to get median
    '''
    length = len(L)
    for i in range(length-1):
        for j in range(length-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L[length//2]


def selectK(L):
    l = len(L)
    if l < 25:
        return median(L)

    n = l // 5
    if l % 5:
        n += 1
    p = []
    for i in range(n):
        begin = i * 5
        end = min(begin + 5, l)
        subL = L[begin:end]
        p.append(median(subL))

    return selectK(p)

k = selectK(datas)
print(k)

