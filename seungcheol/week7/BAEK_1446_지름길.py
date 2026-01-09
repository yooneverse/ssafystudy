from heapq import heappush, heappop

# dijkstra 풀이
def dijkstra():
    pq = [(0, 0)]

    while pq:
        d, now = heappop(pq)

        if dists[now] < d:
            continue

        for nxt, w in short_cut[now]:
            if nxt > D:
                continue

            if dists[nxt] <= d + w:
                continue
            dists[nxt] = d + w
            heappush(pq, (dists[nxt], nxt))

N, D = map(int, input().split())

cnt = 0
short_cut = [[] for _ in range(D + 1)]
for _ in range(N):
    start, end, dist = map(int, input().split())
    if end > D:
        continue
    short_cut[start].append((end, dist))

for i in range(D):
    short_cut[i].append((i + 1, 1))

INF = float("inf")
dists = [INF] * (D + 1)
dists[0] = 0

dijkstra()

print(dists[D])

# dp? 풀이
def dp():
    while node:
        s_node, e_node, d = heappop(node)

        if dists[e_node] <= dists[s_node] + d:
            continue

        dists[e_node] = dists[s_node] + d

        for k in key:
            if e_node >= k:
                continue
            if dists[e_node] + k - e_node >= dists[k]:
                continue
            dists[k] = dists[e_node] + k - e_node

N, D = map(int, input().split())

node = []
dists = {}
dists[D] = D

for _ in range(N):
    start, end, dist = map(int, input().split())
    heappush(node, (start, end, dist))
    dists[start] = start
    dists[end] = end

key = list(dists.keys())
if D not in key:
    key += [D]
key.sort(reverse=True)

dp()

answer = 0

for i in range(len(key) - 1):
    if key[i] > D:
        continue
    answer += dists[key[i]] + (D - key[i])
    break
if answer:
    print(answer)
else:
    print(D)
