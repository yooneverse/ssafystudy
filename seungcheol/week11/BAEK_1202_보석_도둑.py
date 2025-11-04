import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, K = map(int, input().split())

jewels = [0] * N
bags = [0] * K

for i in range(N):
    jewels[i] = tuple(map(int, input().split()))

jewels.sort()

for j in range(K):
    bags[j] = int(input())

bags.sort()

jewel = 0
answer = 0
tmp = []

for bag in bags:
    while jewel < N and jewels[jewel][0] <= bag:
        heappush(tmp, -jewels[jewel][1])
        jewel += 1
    if tmp:
        answer -= heappop(tmp)

print(answer)
