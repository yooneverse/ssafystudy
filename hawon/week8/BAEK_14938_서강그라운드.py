from heapq import heappush, heappop

def dijkstra(start):
    visited = [INF] * (N+1)   # 매번 초기화
    visited[start] = 0
    heap = [(0, start)]

    while heap:
        road, node = heappop(heap)

        if visited[node] < road:
            continue

        for next_r, next_n in graph[node]:
            new_r = next_r + road
            if visited[next_n] > new_r:   # 더 짧으면 갱신
                visited[next_n] = new_r
                heappush(heap, (new_r, next_n))

    return visited


# 지역 개수, 수색범위, 길의 개수
N, M, R = map(int ,input().split())
item_lst = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a].append((l, b))
    graph[b].append((l, a))   # 양방향 추가

INF = float('inf')
answer = 0

# 모든 정점을 시작점으로 다익스트라 실행
for i in range(1, N+1):
    dist = dijkstra(i)
    total = 0
    for j in range(1, N+1):
        if dist[j] <= M:
            total += item_lst[j]
    answer = max(answer, total)

print(answer)
