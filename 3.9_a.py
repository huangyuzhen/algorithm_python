'''
乘方运算
减治方法
复杂度从O(n)减少为O(log(n))
'''

def power2(a, n):
    if n == 1:
        return a
    if n % 2 == 0:
        answer = power2(a, n//2)
        return answer * answer
    else:
        answer = power2(a, (n-1)//2)
        return answer * answer * a



a = 2
b = power2(a, 30)
print(b)
