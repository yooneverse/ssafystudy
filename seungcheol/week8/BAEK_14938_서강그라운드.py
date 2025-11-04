import sys
input = sys.stdin.readline

from heapq import heappush, heappop

def dijkstra(start):
    dists = [INF] * (1 + n)

    pq = [(0, start)]
    dists[start] = 0
    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for nxt_dist, nxt_node in edge[node]:
            new_dist = dist + nxt_dist
            if dists[nxt_node] <= new_dist:
                continue
            dists[nxt_node] = new_dist
            heappush(pq, (new_dist, nxt_node))

    return dists

n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))

edge = [[] for _ in range(n + 1)]

INF = float("inf")

for _ in range(r):
    a, b, l = map(int, input().split())

    edge[a].append((l, b))
    edge[b].append((l, a))

answer = 0
for i in range(1, 1 + n):
    dists = dijkstra(i)

    tmp = 0
    for j in range(1, 1 + n):
        if dists[j] > m:
            continue
        tmp += item[j]
    answer = max(answer, tmp)

print(answer)
