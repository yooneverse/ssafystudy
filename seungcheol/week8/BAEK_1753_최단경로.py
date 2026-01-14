from heapq import heappush, heappop
import sys

input = sys.stdin.readline

def dijkstra():
    dists = [INF] * (V + 1)
    pq = [(0, K)]
    dists[K] = 0
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

V, E = map(int, input().split())
K = int(input())
INF = float("inf")
edge = [[] for _ in range(V + 1)]


for _ in range(E):
    s, e, d = map(int, input().split())
    edge[s].append((d, e))

result = dijkstra()

for i in range(1, 1 + V):
    if result[i] == INF:
        print("INF")
    else:
        print(result[i])
