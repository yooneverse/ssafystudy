import sys
input = sys.stdin.readline

from math import ceil

n, l = map(int, input().split())

cnt = last = answer = 0
waterfall = []

for _ in range(n):
    s, e = map(int, input().split())
    waterfall.append((s, e))

waterfall.sort()

for s, e in waterfall:
    last = max(last, s)
    cnt = ceil((e - last) / l)
    answer += cnt
    last += cnt * l

print(answer)
