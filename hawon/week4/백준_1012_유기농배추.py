from collections import deque

# bfs 만들기
def bfs(r, c, visited):
    q = deque([r, c])
    visited[r][c] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        qr, qc = q.popleft()

        for dr, dc in range(4):
            nr = qr + dr
            nc = qc + dc

            if 0 <= nr < N and 0 <= nc < M and (graph[nr][nc] == 1) and (visited[nr][nc] ==0):
                visited = [nr][nc] = 1
                q.append([nr, nc])

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    # 입력되는 좌표 받아주기 위해서 빈 리스트 만들기
    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    # 해당되는 좌표에 1 추가하기
    for i in range(K):
        r, c = map(int, input().split())
        graph[r][c] = 1

    worm = 0

    for r in range(N):
        for c in range(M):
            if list[r][c] == 1 and visited[r][c] == 0:
                worm += 1
                bfs(r, c, visited)

