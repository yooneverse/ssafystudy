import sys
input = sys.stdin.readline

from heapq import heappop, heappush

N = int(input().strip())

hq = []

for _ in range(N):
    node = list(map(int, input().split()))
    if node[0] == 0:
        if hq:
            print(-heappop(hq))
        else:
            print(-1)
    else:
        for i in range(node[0]):
            heappush(hq, -node[1 + i])
