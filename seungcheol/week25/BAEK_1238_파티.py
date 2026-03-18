import sys
input = sys.stdin.readline

from heapq import heappop, heappush
INF = float("inf")

def dijkstra(start, line):
    dist = [INF] * (n + 1)
    dist[start] = 0

    nodes = [(0, start)]

    while nodes:
        d, node = heappop(nodes)

        if dist[node] < d:
            continue

        for nxt, nd in line[node]:
            if dist[nxt] <= d + nd:
                continue
            dist[nxt] = d + nd
            heappush(nodes, (d + nd, nxt))

    return dist

n, m, x = map(int ,input().split())

forward = [[] for _ in range(n + 1)]
backward = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, t = map(int, input().split())

    forward[s].append((e, t))
    backward[e].append((s, t))

answer1 = dijkstra(x, forward)
answer2 = dijkstra(x, backward)

answer = 0

for i in range(1, n + 1):
    answer = max(answer, answer1[i] + answer2[i])

print(answer)
