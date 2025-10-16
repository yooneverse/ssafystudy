# BAEK 1202. 보석 도둑
import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappop, heappush

N, K = map(int, input().split())
jewels = []
for _ in range(N):
    M, V = map(int, input().split())
    jewels.append((M, V))
jewels.sort()

bags = [int(input()) for _ in range(K)]
bags.sort()

pq = []
value = i = 0

for k in bags:
    while i < N and jewels[i][0] <= k:
        heappush(pq, -jewels[i][1])
        i += 1

    if pq:
        value -= heappop(pq)

print(value)
