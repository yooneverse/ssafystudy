# prim
# 임의의 정점에서 시작, 최소 가중치 연결
# 우선순위큐(힙) 사용
# 인접행렬 또는 리스트 사용
from heapq import heappush, heappop

def prim(start):
    # 방문 배열
    visited = [0] * (V + 1)
    # (간선 가중치, 도착 정점)
    heap = ([(0, start)])

    # MST 누적 비용
    total = 0
    # MST에 포함된 정점 수 (V개가 되면 완성)
    picked = 0

    # while: 아직 선택하지 않은 정점이 있고, 후보 간선이 남아 있을 때 반복
    while heap and picked < V:
        cost, node = heappop(heap)

        # 이미 MST에 들어간 정점이면 버리고 다음 후보 보기
        if visited[node]:
            continue

        # 현재 정점을 MST에 포함
        visited[node] = 1
        picked += 1
        total += cost

        # 현재 정점에서 갈 수 있는 모든 간선 후보를 힙에 넣기
        for next_cost, nxt in graph[node]:
            # 아직 MST에 없는 정점만 후보로 추가
            if not visited[nxt]:
                heappush(heap, (next_cost, nxt))

    return total


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))


print(prim(1))