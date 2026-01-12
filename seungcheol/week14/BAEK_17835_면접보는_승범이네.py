import sys
input = sys.stdin.readline

from heapq import heappop, heappush

def dijkstra():
    dists = [INF] * (N + 1)
    pq = []
    for g in goal:
        heappush(pq, (0, g))
        dists[g] = 0

    while pq:
        dist, start = heappop(pq)

        if dists[start] < dist:
            continue

        for nxt_dist, nxt in edges[start]:
            if dists[nxt] <= dist + nxt_dist:
                continue
            dists[nxt] = dist + nxt_dist
            heappush(pq, (dist + nxt_dist, nxt))

    max_city = 0
    max_dist = 0
    for i in range(1, N + 1):
        if max_dist < dists[i]:
            max_dist = dists[i]
            max_city = i
    return max_city, max_dist

N, M, K = map(int, input().split())

edges = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, d = map(int, input().split())
    edges[e].append((d, s))

goal = list(map(int, input().split()))

INF = float('inf')
answer = dijkstra()

print(answer[0])
print(answer[1])
