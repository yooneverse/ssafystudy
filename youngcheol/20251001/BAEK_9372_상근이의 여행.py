from collections import deque

# 가장 적은 종류의 비행기를 타고 모든 국가들을 여행

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N : 국가 수
    # M : 비행기의 종류

    edge = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        edge[a].append(b)  # 무방향
        edge[b].append(a)

    visited = [0] * (N + 1)
    q = deque([1])
    visited[1] = 1

    cnt = 0  # 간선수
    while q:
        x = q.popleft()
        for i in edge[x]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
                cnt += 1

    print(cnt)
