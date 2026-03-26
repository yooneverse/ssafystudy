import sys
input = sys.stdin.readline

from collections import deque

n = int(input().strip())

balloon = list(map(int, input().split()))
que = deque((i + 1, balloon[i]) for i in range(n))

answer = []

for _ in range(n):
    idx, b = que.popleft()
    answer.append(idx)

    if b > 0:
        que.rotate(-b + 1)
    else:
        que.rotate(-b)

print(*answer)
