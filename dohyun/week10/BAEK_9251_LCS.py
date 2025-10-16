# BAEK 9251. LCS
import sys
sys.stdin = open('input.txt', 'r')

a = input()
b = input()

# (len(a) + 1, len(b) + 1) 배열
# [[0, 0, 0, 0, 0, 0, 0]
# [0, 0(여기서 시작), 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]]
dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(a)][len(b)])