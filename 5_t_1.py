'''
删数字游戏
'''

def deleteNumber(n, s):
    number = str(n)

    for _ in range(s):
        length = len(number)
        for i in range(length-1):
            a = number[i]
            b = number[i+1]
            if a > b:
                number = number[:i] + number[i+1:]
                break
        else:
            number = number[:-1]

    return number

line = input().split(" ")
n = int(line[0])
s = int(line[1])

print(deleteNumber(n, s))

'''
输入
178543 4
输出
13
'''
