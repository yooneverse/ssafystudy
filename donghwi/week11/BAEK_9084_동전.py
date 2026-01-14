# https://www.acmicpc.net/problem/9084
T = int(input())

for _ in range(T):
    N = int(input())

    coin = [0] + list(map(int, input().split()))
    goal = int(input())

    dp = [[0] * (goal + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = 1

    for y in range(1, N + 1):
        for x in range(1, goal + 1):
            dp[y][x] = dp[y - 1][x]
            if x - coin[y] >= 0:
                dp[y][x] += dp[y][x-coin[y]]

    print(dp[N][goal])