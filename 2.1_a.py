'''
水仙花数
153 ＝ 1^3 + 5^3 + 3^3
找出所有水仙花数
'''


for i in range(100,1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if i == a*a*a + b*b*b + c*c*c:
        print(i)
