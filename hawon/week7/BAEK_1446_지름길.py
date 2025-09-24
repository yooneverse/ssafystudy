from heapq import heappop, heappush

def dijkstra(start_node):
    # 가중치, 노드
    heap = [(0, start_node)]
    # 시작점까지의 최단거리는 0으로 설정
    visited[start_node] = 0

    while heap:
        dist, node = heappop(heap)

        # 이미 더 짧은 경로로 방문한 적이 있으면 스킵 (가지치기)
        if visited[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = next_dist + dist

            # 기존에 알고 있던 next_node까지의 최단거리보다 더 짧으면 갱신
            if visited[next_node] > new_dist:
                visited[next_node] = new_dist
                # 더 좋은 경로가 생겼으니 큐에 넣기
                heappush(heap, (new_dist, next_node))

# 지름길 개수 N, 고속도로 길이 D
N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
for _ in range(N):
    s, e, w = map(int, input().split())
    # 고속도로 종점 D를 넘는 지름길은 의미 없음 → 무시
    if e > D:
        continue
    graph[s].append((w, e))

# 지름길 안 써도 항상 D까지 도달할 수 있게 보장
for i in range(D):
    graph[i].append((1, i+1))

INF = float('inf')
visited = [INF] * (D+1)

dijkstra(0)

print(visited[D])