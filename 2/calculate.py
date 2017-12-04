#!/usr/bin/env python3

total = 0
for line in open('input.txt', 'r').readlines():
    nums = line.split()
    small = min((int(n) for n in nums))
    big = max((int(n) for n in nums))
    total += big - small

print(total)
