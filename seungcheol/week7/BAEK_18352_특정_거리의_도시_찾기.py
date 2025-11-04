from heapq import heappush, heappop

N, M, K, X = map(int, input().split())

def dijkstra(start_node):
    pq = [(0, start_node)]

    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)

        if dist > dists[node]:
            continue


        for next_node in edge[node]:
            if dists[next_node] <= dist + 1:
                continue
            dists[next_node] = dist + 1
            heappush(pq, (dists[next_node], next_node))


edge = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    edge[start].append(end)

dists = [float("inf")] * (N + 1)

dijkstra(X)

if dists.count(K):
    for i in range(1, N + 1):
        if dists[i] == K:
            print(i)
else:
    print(-1)