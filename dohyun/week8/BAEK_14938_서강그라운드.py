# BAEK 14938. 서강그라운드
# 힙 사용
from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt', 'r')

n, m, r = map(int, input().split())
t = list(map(int, input().split()))

# 인접 리스트 생성
# 정점의 번호가 1부터 시작하므로 (n + 1) 개
adj = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    # 정점마다 값을 더해줘야 하므로 양방향
    adj[a].append((l, b))
    adj[b].append((l, a))


# 다익스트라 함수 정의
# 시작점을 인자로 받음
def dijkstra(s):
    # 힙 생성
    pq = [(0, s)]
    # 정점별 최소 거리 구하기 위해 극한값의 배열 설정
    best = [float('inf')] * (n + 1)
    # 시작점의 최소 거리는 0
    best[s] = 0

    # 힙에 원소가 존재하면 반복
    while pq:
        # 힙에서 현재 노드와 현재 노드까지의 거리 꺼냄
        # 만약 거리가 갈 수 있는 거리보다 크거나
        # 도달 가능한 최소 거리보다 크면 넘어감
        dist, node = heappop(pq)
        if dist > m or best[node] < dist:
            continue

        # 인접 리스트에서 다음 노드와 다음 노드까지의 거리 꺼내고
        # 현재 노드까지의 거리와 다음 노드까지의 거리를 더함
        for n_dist, n_node in adj[node]:
            n_dist = dist + n_dist

            # 만약 더한 거리가 갈 수 있는 거리나 최소 거리보다 크면 넘어감
            if n_dist > m or best[n_node] <= n_dist:
                continue

            # 다음 노드까지의 최소 거리를 더한 거리로 설정
            # 힙에 추가
            best[n_node] = n_dist
            heappush(pq, (n_dist, n_node))

    # 최소 거리 배열 반환
    return best


# 결과값 변수 생성
ans = 0
# 1번 노드부터 n번 노드까지 반복해서 다익스트라 실행
for i in range(1, n + 1):
    arr = dijkstra(i)
    # 노드의 값을 더해줄 변수 초기화
    item = 0
    # i번 노드에서 j번 노드로 갈 수 있을 때
    # 노드의 값을 다 더해줌
    for j in range(1, n + 1):
        if arr[j] != float('inf'):
            item += t[j - 1]
    # 갈 수 있는 노드의 총합과 결과값 비교해서 큰 값 도출
    ans = max(item, ans)

print(ans)
