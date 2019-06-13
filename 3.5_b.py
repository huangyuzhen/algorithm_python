'''
楼梯有n阶，可以一步上1阶，2阶，3阶，问有多少种不同的走法。
n<=1000000
'''

StepResult = {0:0, 1:1, 2:2, 3: 4}
def floor(n):
    mod = int(1e9+7)
    global StepResult

    s = StepResult.get(n)
    if s == None:
        s = floor(n-1) + floor(n-2) + floor(n-3)
        StepResult[n] = s % mod

    return s

print(floor(4))
