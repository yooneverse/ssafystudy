# BAEK_1012_유기농_배추
from collections import deque

T = int(input())
d = (-1, 0), (1, 0), (0, -1), (0, 1)


def DFS(r, c):
    visited[r][c] = 1
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and cabbage[nr][nc] == 1 and visited[nr][nc] == 0:
            DFS(nr, nc)


def BFS(row, col):
    dq = deque()
    dq.append((row, col))
    visited[row][col] = 1
    while dq:
        r, c = dq.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and cabbage[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                dq.append((nr, nc))


for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    cabbage = [[0] * M for _ in range(N)]

    for n in range(K):
        (x, y) = map(int, input().split())
        cabbage[y][x] += 1

    visited = [[0] * M for _ in range(N)]
    bug = 0

    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1 and visited[i][j] == 0:
                # DFS(i, j)
                BFS(i, j)
                bug += 1

    print(bug)
