from collections import deque


def BFS(x, y, z):
    qu = deque()
    qu.append((x, y, z))

    while qu:
        i, j, k = qu.popleft()

        if i == N - 1 and j == M - 1:
            return visited[i][j][k]

        for d in range(4):
            nr = i + dr[d]
            nc = j + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and k == 0:
                    visited[nr][nc][1] = visited[i][j][0] + 1
                    qu.append((nr, nc, 1))
                elif arr[nr][nc] == 0 and visited[nr][nc][k] == 0:
                    visited[nr][nc][k] = visited[i][j][k] + 1
                    qu.append((nr, nc, k))

    return -1


N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


visited[0][0][0] = 1

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

print(BFS(0, 0, 0))
