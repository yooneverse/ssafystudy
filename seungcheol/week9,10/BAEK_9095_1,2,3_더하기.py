import sys
input = sys.stdin.readline

t = int(input().strip())

dp = [0] * 12
dp[0] = 1
cnt = 0
for _ in range(t):
    num = int(input().strip())

    if num > cnt:
        for i in range(cnt, num):
            for j in range(1, 4):
                if i + j < 12:
                    dp[i + j] += dp[i]
        cnt = num
    print(dp[num])

