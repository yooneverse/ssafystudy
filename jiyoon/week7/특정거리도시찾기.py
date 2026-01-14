from collections import deque

# 도시 개수 N, 도로 개수 M, 거리 K, 출발 도시 X 입력
N, M, K, X = map(int, input().split())

# 인접 리스트 형태로 그래프 저장 (도시 번호: 1~N)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

# 최단 거리 기록할 리스트 distance 초기화 (-1로 채움)
# 출발 도시 X의 거리는 0으로 설정
dist = [-1] * (N+1)
dist[X] = 0

# BFS 시작을 위해 큐에 출발 도시 X를 넣음
q = deque([X])

# 큐에서 하나씩 꺼내면서 인접 도시 탐색
#   아직 방문하지 않은 도시라면 (distance == -1)
#       현재 도시 거리 + 1 을 다음 도시의 거리로 기록
#       큐에 넣어서 계속 탐색
while q:
    now = q.popleft()
    for nxt in graph[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1
            q.append(nxt)

# BFS가 끝난 후, distance 배열을 확인
#   거리가 정확히 K인 도시 번호만 출력
#   하나도 없으면 -1 출력
found = False
for i in range(1, N+1):
    if dist[i] == K:
        print(i)
        found = True
if not found:
    print(-1)

