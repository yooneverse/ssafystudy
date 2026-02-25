# BAEK 1463. 1로 만들기
import sys
input = sys.stdin.readline

N = int(input())

# 연산 3가지
# 1. X % 3 = 0 이면 3으로 나눈다
# 2. X % 2 = 0 이면 2로 나눈다
# 3. X - 1

# bottom-up
dp = [0] * (N + 1)
for i in range(2, N + 1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])
    
