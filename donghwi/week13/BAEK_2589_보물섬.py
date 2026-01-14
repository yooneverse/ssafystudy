# https://www.acmicpc.net/problem/2589
from collections import deque


def bfs(y, x):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    qu.append((y, x))
    visited = [[-1] * M for _ in range(N)]
    visited[y][x] = 0
    result = 0
    while qu:
        i, j = qu.popleft()

        for d in range(4):
            nr = i + dr[d]
            nc = j + dc[d]

            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 'L' and visited[nr][nc] == -1:
                visited[nr][nc] = visited[i][j] + 1
                result = max(result, visited[nr][nc])
                qu.append((nr, nc))
    return result


N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

qu = deque()
final_result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            final_result = max(final_result, bfs(i, j))

print(final_result)
