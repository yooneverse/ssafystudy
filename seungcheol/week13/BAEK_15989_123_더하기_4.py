import sys
input = sys.stdin.readline

T = int(input().strip())


n = [int(input().strip()) for _ in range(T)]
max_n = max(n)
dp = [1] * (max_n + 1)

for i in (2, 3):
    for j in range(max_n + 1 - i):
        dp[j + i] += dp[j]

for i in n:
    print(dp[i])
