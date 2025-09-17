import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def dfs(i, j):
    # 종료지점 도착
    if i == M - 1 and j == N - 1:
        return 1

    # 이미 온 적 있는 경로면
    if dp[i][j] > -1:
        return dp[i][j]

    # 이동 가능한 경로
    dp[i][j] = 0

    # 내리막길 인지 확인
    for di, dj in delta:
        ni = i + di
        nj = j + dj
        if ni < 0 or ni >= M or nj < 0 or nj >= N:
            continue
        if matrix[i][j] > matrix[ni][nj]:
            dp[i][j] += dfs(ni, nj)

    return dp[i][j]

M, N = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

print(dfs(0, 0))
