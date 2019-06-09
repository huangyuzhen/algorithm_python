'''
百钱百鸡问题
鸡翁一，值钱五，鸡母一，值钱三，鸡雏三，值钱一。百钱买百鸡

m钱n鸡
'''

M = 100
N = 100

print('#1')
# 三重循环
for n1 in range(N):
    for n2 in range(N):
        for n3 in range(N):
            if n1 + n2 + n3 == N and 5*n1 + 3 * n2 + n3 / 3 == M:
                print(n1, n2, n3)

print('#2')
# 优化
for n1 in range(N//5):
    for n2 in range(N//3):
        n3 = N - (n1 + n2)
        if 5*n1 + 3*n2 + n3/3 == M:
            print(n1, n2, n3)

'''
设计不同的枚举对象，简化算法
'''
