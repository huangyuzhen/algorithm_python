'''
回溯算法
程序模版
'''

S = ['0'] * 10
Count = 0

def backtrack(t, n):
    global Count
    if t >= n:
        Count += 1
        # print("".join(S))
        return
    else:
        S[t] = '1'
        backtrack(t+1, n)

        S[t] = '0'
        backtrack(t+1, n)

backtrack(0, len(S))
print(Count)
