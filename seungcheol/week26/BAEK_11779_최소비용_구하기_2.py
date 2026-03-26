import sys

input = sys.stdin.readline

from heapq import heappop, heappush

INF = float("inf")


def dijkstra(start, end):
    dists = [INF] * (n + 1)
    dists[start] = 0

    adj = [[] for _ in range(n + 1)]
    adj[start] = [start]

    pq = [(0, start)]

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for nxt, ndist in edges[node]:
            pdist = dist + ndist
            if dists[nxt] <= pdist:
                continue
            heappush(pq, (pdist, nxt))
            tmp = adj[node][:]
            tmp.append(nxt)
            adj[nxt] = tmp
            dists[nxt] = pdist

    return dists[end], len(adj[end]), adj[end]


n = int(input().strip())
m = int(input().strip())

edges = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, d = map(int, input().split())
    edges[s].append((e, d))

enter, goal = map(int, input().split())

answer = dijkstra(enter, goal)

print(answer[0])
print(answer[1])
print(*answer[2])
