import sys
input = sys.stdin.readline

import math

def check(num):
    r = int(math.sqrt(num))
    for k in range(3, r + 1, 2):
        if num % k == 0:
            return False
    return True

def find(num, level):
    if level == n:
        print(num)
        return

    for j in (1, 3, 5, 7, 9):
        tmp = num * 10 + j
        if check(tmp):
            find(tmp, level + 1)

n = int(input().strip())

for i in (2, 3, 5, 7):
    find(i, 1)
