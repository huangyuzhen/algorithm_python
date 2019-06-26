#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def greedyNumber(number, k):
    for _ in range(k):
        n = len(number)
        for i in range(n-1):
            if number[i] < number[i+1]:
                number = number[:i] + number[i+1:]
                break
        else:
            number = number[:-1]

    return number


number = input("input number: ")
k = int(input("input k: "))

print(greedyNumber(number,k))
