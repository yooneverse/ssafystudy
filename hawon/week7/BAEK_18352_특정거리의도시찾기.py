from heapq import heappop, heappush

def dijkstra(start):
    # 가중치, 노드
    heap = [(0, start)]
    visited[start] = 0

    while heap:
        w, n = heappop(heap)

        if visited[n] < w:
            continue

        for next_w, next_n in graph[n]:
            new_w = next_w + w

            # 기존에 알고 있던 next_node까지의 최단거리보다 더 짧으면 갱신
            if visited[next_n] > new_w:
                visited[next_n] = new_w
                heappush(heap, (new_w, next_n))

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((1, b))

INF = float('inf')
visited = [INF] * (N+1)

dijkstra(X)

result = []
# 거리 K인 도시들만 출력
for i in range(1, N+1):
    if visited[i] == K:
        result.append(i)

if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)
