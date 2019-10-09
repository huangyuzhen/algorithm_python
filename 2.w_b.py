#!/usr/bin/env python3

def division(n, factor):
    r = n % factor
    while r == 0:
        n = n // factor
        r = n % factor

    return n

def isLuckyNumber(n):
    n = division(n, 3)
    n = division(n, 5)
    n = division(n, 7)

    return n==1


x = input("input number: ")
if x != '':
    x = int(x)
    count = 0
    for i in range(3, x+1):
        if isLuckyNumber(i):
            count += 1

print(count)
