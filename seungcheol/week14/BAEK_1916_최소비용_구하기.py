import sys
input = sys.stdin.readline

from heapq import heappop, heappush

def dijkstra():
    dists = [INF] * (N + 1)
    pq = [(0, start)]
    dists[start] = 0
    while pq:
        dist, nxt = heappop(pq)
        if dists[nxt] < dist:
            continue

        for n_dist, city in cities[nxt]:
            if dists[city] <= dist + n_dist:
                continue
            dists[city] = dist + n_dist
            heappush(pq, (dist + n_dist, city))

    return dists[end]

N = int(input().strip())
M = int(input().strip())

cities = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, d = map(int, input().split())
    cities[s].append((d, e))

INF = float('inf')

start, end = map(int, input().split())

answer = dijkstra()

print(answer)
