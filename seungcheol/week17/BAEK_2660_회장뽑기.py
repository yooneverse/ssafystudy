import sys
input = sys.stdin.readline

from heapq import heappop, heappush

def dijkstra(start):
    dists = [51] * (N + 1)
    dists[0] = 0
    dists[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for nxt_node in edge[node]:
            nxt_dist = dist + 1
            if dists[nxt_node] <= nxt_dist:
                continue
            dists[nxt_node] = nxt_dist
            heappush(pq, (nxt_dist, nxt_node))

    return max(dists)

N = int(input().strip())
edge = [[] for _ in range(N + 1)]

while True:
    s, e = map(int, input().split())

    if s == -1:
        break

    edge[s].append(e)
    edge[e].append(s)

scores = [51] * (N + 1)
for i in range(1, N + 1):
    scores[i] = dijkstra(i)

score = min(scores)
num = 0
answer = []

for j in range(1, N + 1):
    if scores[j] == score:
        num += 1
        answer.append(j)

print(score, num)
print(*answer)
