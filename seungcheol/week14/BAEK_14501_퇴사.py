import sys
input = sys.stdin.readline

# bruteforce 풀이
# def brute(score, idx):
#     global answer
#     if idx >= N:
#         answer = max(answer, score)
#         return
#
#     for i in range(idx, N):
#         days, fee = schedule[i]
#         if i + days <= N:
#             brute(score + fee, i + days)
#
#     answer = max(answer, score)
#     return
# N = int(input().strip())
#
# schedule = [0] * N
#
# for i in range(N):
#     schedule[i] = tuple(map(int, input().split()))
#
# answer = 0
# brute(0, 0)
#
# print(answer)

# dp 풀이
N = int(input().strip())

schedule = [0] * N

for i in range(N):
    schedule[i] = tuple(map(int, input().split()))

dp = [0] * (N + 1)

answer = 0

for i in range(N - 1, -1, -1):
    if i + schedule[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], schedule[i][1] + dp[i + schedule[i][0]])
print(dp[0])
