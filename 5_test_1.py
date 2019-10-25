#!/usr/bin/env python3

def greedyNumber(number, k):
    length = len(number)
    if k >= length:
        return ""

    for _ in range(k):
        for i in range(length-1):
            if number[i] < number[i+1]:
                number = number[:i] + number[i+1:]
                break
        else:
            number = number[:-1]
        length -= 1

    return number


line = input().split()
n = str(line[0])
k = int(line[1])

number = greedyNumber(n, k)
print(number)
