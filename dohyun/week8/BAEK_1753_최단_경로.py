# BAEK 1753. 최단 경로
# 힙 사용
from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())
K = int(input())

# 인접 리스트 생성
# 정점의 번호가 1부터 시작하므로 (n + 1) 개
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    # 잘 모르겠음
    adj[u].append((w, v))


# 다익스트라 함수 정의
# 시작점을 인자로 받음
def dijkstra(s):
    # 힙 생성
    pq = [(0, s)]
    # 정점별 최소 거리 구하기 위해 극한값의 배열 설정
    best = [float('inf')] * (V + 1)
    # 시작점의 최소 거리는 0
    best[s] = 0

    # 힙에 원소가 존재하면 반복
    while pq:
        # 힙에서 현재 노드와 현재 노드까지의 거리 꺼냄
        # 만약 거리가 최소 거리보다 크면 넘어감
        dist, n = heappop(pq)
        if best[n] < dist:
            continue

        # 인접 리스트에서 다음 노드와 다음 노드까지의 거리 꺼내고
        # 현재 노드까지의 거리와 다음 노드까지의 거리를 더함
        for n_dist, n_n in adj[n]:
            n_dist = dist + n_dist

            # 만약 더한 거리가 최소 거리보다 크면 넘어감
            if best[n_n] <= n_dist:
                continue

            # 다음 노드까지의 최소 거리를 더한 거리로 설정
            # 힙에 추가
            best[n_n] = n_dist
            heappush(pq, (n_dist, n_n))

    # 최소 거리 배열 반환
    return best


# 시작값 K로 설정 후 다익스트라 함수 실행
arr = dijkstra(K)

# i번 노드에서 j번 노드로 갈 수 있을 때
# 거리 출력
for i in range(1, V + 1):
    if arr[i] != float('inf'):
        print(arr[i])
    # 갈 수 없으면 INF 출력
    else:
        print('INF')
