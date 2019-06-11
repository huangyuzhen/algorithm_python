'''
斯特林数 Stirling 数
n个元素的集合{1,2,...,n}可以划分为若干个非空子集合的集合。例如，n＝3时，
集合{1,2,3}可以划分为5个不同的非空子集合的集合，如下:
{{1},{2},{3}}
{{1,2}, {3}}
{{1,3}, {2}}
{{2,3}, {1}
{{1,2,3}}

'''


def Stirling(n, m):
    if m == 0 or m > n:
        count = 0
    elif m == 1 or m == n:
        count = 1
    else:
        a = Stirling(n-1, m) * m
        b = Stirling(n-1, m-1)
        count = a + b

    # print(n, m, count)
    return count

s = Stirling(5, 2)
print(s)

'''
运用:
把n个不同的苹果放入m个相同的盘子种，不允许盘子为空，请问总共有多少种方法?

'''
