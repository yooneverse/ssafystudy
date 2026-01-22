import sys
input = sys.stdin.readline

N = int(input().strip())
house = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0][0], dp[0][1], dp[0][2] = house[0][0], house[0][1], house[0][2]

for j in range(1, N):
    dp[j][0] = min(dp[j - 1][1] + house[j][0], dp[j - 1][2] + house[j][0])
    dp[j][1] = min(dp[j - 1][0] + house[j][1], dp[j - 1][2] + house[j][1])
    dp[j][2] = min(dp[j - 1][0] + house[j][2], dp[j - 1][1] + house[j][2])

print(min(dp[N - 1]))
