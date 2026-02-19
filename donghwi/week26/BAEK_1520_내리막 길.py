import sys
sys.setrecursionlimit(10**6)
def DFS(y, x):
    if (y, x) == (N - 1, M - 1):
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    center = matrix[y][x]

    way = 0

    for d in range(4):
        nr = y + dr[d]
        nc = x + dc[d]

        if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] < center:
            way += DFS(nr, nc)

    dp[y][x] = way
    return dp[y][x]


N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * M for _ in range(N)]

print(DFS(0, 0))
