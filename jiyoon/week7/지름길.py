import heapq

N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]

# 인접 리스트 그래프 초기화
graph = [[] for _ in range(D+1)]

# 1) 일반 도로 연결 (i -> i+1, 비용 1)
for i in range(D):
    graph[i].append((i+1, 1))

# 2) 지름길 연결
for s, e, l in shortcuts:
    if e <= D:   # 고속도로 끝 넘으면 무효
        graph[s].append((e, l))

# 다익스트라
INF = int(1e9)
dist = [INF] * (D+1)
dist[0] = 0
pq = [(0, 0)]  # (비용, 노드)

while pq:
    cost, now = heapq.heappop(pq)
    if dist[now] < cost:
        continue

    for nxt, w in graph[now]:
        new_cost = cost + w
        if new_cost < dist[nxt]:
            dist[nxt] = new_cost
            heapq.heappush(pq, (new_cost, nxt))

print(dist[D])