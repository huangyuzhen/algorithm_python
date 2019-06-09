'''
绳子切割问题

有N条绳子，他们的长度分别为L(i) (<=1000).如果从他们当中切割出k条长度相同的绳子的话，
这k条绳子每条最长能有多长? 答案保留到小数点后2位
'''

L = [8.02, 7.43, 4.57, 5.39]
N = len(L)
K = 11

length = 0
for i in range(100000):
    length += 0.01

    k = 0
    for l in L:
        k += int(l / length)

    if k>= K:
        print(k,length)

'''
时间复杂度 O(n)
'''
