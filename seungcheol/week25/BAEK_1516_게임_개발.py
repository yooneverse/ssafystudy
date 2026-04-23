import sys

input = sys.stdin.readline

n = int(input().strip())

dp = [0] * (n + 1)
times = [0] * (n + 1)
edges = [0] * (n + 1)

for i in range(1, n + 1):
    time, *edge = map(int, input().split())
    times[i] = time
    edges[i] = edge[:-1]


def game(start):
    base = 0
    for e in edges[start]:
        if not dp[e]:
            game(e)
        base = max(base, dp[e])

    dp[start] = base + times[start]


for i in range(1, n + 1):
    if dp[i]:
        continue
    game(i)

for answer in dp[1:]:
    print(answer)
