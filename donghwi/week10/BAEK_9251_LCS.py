# 두 문자열 입력 받기
S1 = input()
S2 = input()

max_stack = 0  # 최장 공통 부분 수열의 최대 길이를 저장할 변수

# DP 테이블 초기화
# dp[i][j]는 S1의 i번째 문자까지와 S2의 j번째 문자까지의
# "최장 공통 부분 수열(LCS)"의 길이를 저장한다.
dp = [[0] * (len(S2) + 1) for _ in range(len(S1) + 1)]

# DP 테이블 채우기
for i in range(1, len(S1) + 1):
    for j in range(1, len(S2) + 1):
        if S1[i - 1] == S2[j - 1]:
            # 두 문자가 같으면, 이전 문자까지의 LCS 길이에 1을 더함
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            # 다르면, 이전 단계에서 가능한 최댓값을 가져옴
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# DP 테이블 출력 및 최댓값 탐색
for i in range(len(S1) + 1):
    print(dp[i])  # 각 행 출력 (디버깅용)
    for j in range(len(S2) + 1):
        max_stack = max(max_stack, dp[i][j])  # LCS 최대 길이 갱신

# 최장 공통 부분 수열의 길이 출력
print(max_stack)