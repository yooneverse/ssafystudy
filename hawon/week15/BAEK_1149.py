import sys
input = sys.stdin.readline

N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]

# 0번 집 (1번 집에 해당)
dp[0][0] = rgb[0][0]  # 빨강
dp[0][1] = rgb[0][1]  # 초록
dp[0][2] = rgb[0][2]  # 파랑

# i: 1 ~ N-1  (배열 기준으로는 2번 집 ~ N번 집)
for i in range(1, N):
    # i번 집을 빨강으로 칠하는 경우
    dp[i][0] = rgb[i][0] + min(dp[i-1][1], dp[i-1][2])
    # i번 집을 초록으로 칠하는 경우
    dp[i][1] = rgb[i][1] + min(dp[i-1][0], dp[i-1][2])
    # i번 집을 파랑으로 칠하는 경우
    dp[i][2] = rgb[i][2] + min(dp[i-1][0], dp[i-1][1])

# 마지막 집은 인덱스로 N-1
answer = min(dp[N-1][0], dp[N-1][1], dp[N-1][2])
print(answer)
