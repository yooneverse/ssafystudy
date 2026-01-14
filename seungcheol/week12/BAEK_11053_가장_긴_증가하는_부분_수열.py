import sys
input = sys.stdin.readline

N = int(input().strip())
num = list(map(int, input().split()))

dp = [1] * N  # dp[i] = num[i]로 끝나는 LIS 길이

for i in range(N):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
