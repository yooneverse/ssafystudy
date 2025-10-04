# 그니까 시작 정점에서, 다른 모든 정점으로 갈 때 길을 출력하라는 거임
# 그러면 다 이동 안해도 되니까 다익스트라
from heapq import heappush, heappop

def dijkstra(start):
    heap = ([(0,start)])
    visited[start] = 0

    while heap:
        weight, node = heappop(heap)

        if visited[node] < weight:
            continue

        for next_w, next_n in graph[node]:
            new_w = weight + next_w

            if visited[next_n] > new_w:
                visited[next_n] = new_w
                heappush(heap, (new_w, next_n))

    return visited

V, E = map(int, input().split())
# 시작 정점
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((w,v))

INF = float('inf')
visited = [INF] * (V+1)
dijkstra(K)


# 출력 (1번부터 V번까지)
for i in range(1, V+1):
    if visited[i] == INF:
        print("INF")
    else:
        print(visited[i])
