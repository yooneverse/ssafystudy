import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = set()

for _ in range(n):
    coins.add(int(input().strip()))

coins = list(coins)
coins.sort()

dp = [10001] * (k + 1)
dp[0] = 0

for i in range(len(coins)):
    for j in range(coins[i], k + 1):
        dp[j] = min(dp[j], dp[j - coins[i]] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])

