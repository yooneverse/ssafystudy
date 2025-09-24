from collections import deque
# 특정한 도시 X로부터 최단거리가 정확히 K인 모든 도시들의 번호 출력
# 없으면 -1 출력

N, M, K, X = map(int, input().split())
# N : 도시 개수
# M : 도로 개수
# K : 거리 정보
# X : 출발 도시 번호
arr = [[] for _ in range(N + 1)] #인접리스트
visited = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)  # 단방향이기에

# 미방문은 -1
dist = [-1] * (N + 1)
dist[X] = 0  #시작점

#BFS 수행
q = deque([X])
while q:
    cur = q.popleft()

    # 현재 정점까지의 최단거리가 이미 K라면, 더 멀리 가면 K+1이므로 확장 x
    if dist[cur] == K:
        continue

    # cur에서 나가는 모든 단방향 간선 탐색
    for nxt in arr[cur]:
        if dist[nxt] != -1:
            # 이미 더 짧은 거리로 방문됨 → 패스
            continue
        dist[nxt] = dist[cur] + 1
        q.append(nxt)

# 결과: 최단거리가 정확히 K인 도시들을 오름차순으로 출력  요건 gpt힘
if K not in dist[1:]:     # dist[0]은 더미(1-기반 인덱스)라 제외
    print(-1)
else:
    for city in range(1, N + 1):
        if dist[city] == K:
            print(city)