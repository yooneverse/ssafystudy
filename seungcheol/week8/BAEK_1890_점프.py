def dfs(r, c):
    if r == n - 1 and c == n - 1:
        return 1

    if grid[r][c] == 0:
        return 0

    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0

    for dr, dc in delta:
        nr, nc = r + dr * grid[r][c], c + dc * grid[r][c]

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue

        dp[r][c] += dfs(nr, nc)

    return dp[r][c]


n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * n for _ in range(n)]

delta = [(0, 1), (1, 0)]

dfs(0, 0)

print(dp[0][0])
