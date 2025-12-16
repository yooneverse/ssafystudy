import sys

N = int(sys.stdin.readline())
costs = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]
'''
000
000
000
000

'''
dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]

for i in range(1,N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

print(min(dp[N-1]))