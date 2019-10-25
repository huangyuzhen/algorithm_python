#!/usr/bin/env python3

def greedyNumber(number, k):
    n = len(number)
    if k >= n:
        return ""

    for _ in range(k):
        for i in range(n-1):
            if number[i] < number[i+1]:
                number = number[:i] + number[i+1:]
                break
        else:
            number = number[:-1]
        n -= 1

    return number


line = input().split()
n = str(line[0])
k = int(line[1])

number = greedyNumber(n, k)
print(number)
