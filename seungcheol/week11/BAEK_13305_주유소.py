import sys
input = sys.stdin.readline

N = int(input())
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))

total = 0
cost = costs[0]
for i in range(N - 1):
    if cost > costs[i]:
        cost = costs[i]
    total += cost * dists[i]
print(total)