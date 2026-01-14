from heapq import heappop, heappush


def dijkstra(start_node):
    global max_farming

    pq = [(0, start_node)]
    dists = [INF] * (N + 1)
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist

            if new_dist > M:
                continue

            # if dists[next_node] <= new_dist:
            #     continue

            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return dists


N, M, R = map(int, input().split())

INF = int(21e8)

max_farming = 0

items = [-1] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for j in range(R):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))

for i in range(1, N + 1):
    farming = 0
    lst = dijkstra(i)

    print(lst)
    for j in range(1, N + 1):
        if lst[j] <= M:
            farming += items[j]

    max_farming = max(max_farming, farming)

print(max_farming)
