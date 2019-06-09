'''
模糊数字问题
'''

print('#1')
d = (1, 9, 'x', 9, 5)
for d2 in range(10):
    number = d[0] * 10000 + d[1] * 1000 + d2 *100 + d[3]* 10 + d[4]
    if number % 57 == 0  and number % 67 == 0:
        print(d2, number)


print('#2')
d = ('x', 9, 'x', 9, 5)
for d0 in range(1,10):
    for d2 in range(0,10):
        number = d0 * 10000 + d[1] * 1000 + d2 *100 + d[3]* 10 + d[4]
        if number % 57 == 0  and number % 67 == 0:
            print(d0, d2, number)

print('#3')
for d in range(100, 1000):
    number = d * 100 + 95
    if number % 57 == 0  and number % 67 == 0:
        print(d, number)


'''
O(n)
'''
