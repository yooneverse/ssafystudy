from collections import deque


def land():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    drx = [-1, 1, 1, -1]
    dcx = [1, 1, -1, -1]
    while qu:
        y, x = qu.popleft()

        for d in range(4):
            nr = y + dr[d]
            nc = x + dc[d]
            nrx = y + drx[d]
            ncx = x + dcx[d]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if world[nr][nc] == 1:
                    visited[nr][nc] = 1
                    qu.append((nr, nc))

            if 0 <= nrx < N and 0 <= ncx < M and visited[nrx][ncx] == 0:
                if world[nrx][ncx] == 1:
                    visited[nrx][ncx] = 1
                    qu.append((nrx, ncx))

    return


while True:

    M, N = map(int, input().split())

    if (N, M) == (0, 0):
        break

    world = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    qu = deque()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if world[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                visited[i][j] = 1
                qu.append((i, j))
                land()

    print(cnt)
