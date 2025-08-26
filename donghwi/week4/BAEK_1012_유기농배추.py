from collections import deque


def BFS(q):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while q:
        global cnt
        di, dj = q.popleft()

        for d in range(4):
            nr = di + dr[d]
            nc = dj + dc[d]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and farm[nr][nc] == 1:
                q.append((nr, nc))
                visited[nr][nc] = 1
    cnt += 1


TestCase = int(input())

for T in range(TestCase):
    M, N, K = map(int, input().split())

    farm = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    qu = deque()
    cnt = 0
    for i in range(K):
        x, y = map(int, input().split())

        farm[y][x] = 1

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and visited[i][j] == 0:
                qu.append((i, j))
                visited[i][j] = 1
                BFS(qu)

    print(cnt)