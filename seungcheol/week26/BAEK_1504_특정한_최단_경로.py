import sys

input = sys.stdin.readline

from heapq import heappop, heappush

INF = float("inf")


def dijkstra(start):
    dists = [INF] * (n + 1)
    dists[start] = 0

    pq = [(0, start)]

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for nxt, ndist in edges[node]:
            pdist = dist + ndist

            if dists[nxt] <= pdist:
                continue

            dists[nxt] = pdist
            heappush(pq, (pdist, nxt))

    return dists


n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, d = map(int, input().split())
    edges[s].append((e, d))
    edges[e].append((s, d))

a, b = map(int, input().split())

first = dijkstra(1)
second = dijkstra(a)
third = dijkstra(b)

answer = min(first[a] + second[b] + third[n], first[b] + second[n] + third[a])

if answer == INF:
    print(-1)
else:
    print(answer)
