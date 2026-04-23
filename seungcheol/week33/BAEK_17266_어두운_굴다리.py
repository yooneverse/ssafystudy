import sys
input = sys.stdin.readline

from math import ceil

n = int(input().strip())
m = int(input().strip())
light = list(map(int, input().split()))

prev = now = answer = 0

for x in light:
    prev = now
    now = x
    if prev:
        answer = max(answer, ceil((now - prev) / 2))
    else:
        answer = now
answer = max(answer, n - now)

print(answer)
