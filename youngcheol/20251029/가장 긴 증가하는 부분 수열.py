N = int(input().strip())
lst = list(map(int, input().split()))

# dp[i] = i번째 원소로 "끝나는" 증가 부분 수열의 최장 길이
# 최소한 자기 자신만 뽑아도 길이 1이므로 1로 시작
dp = [1] * N

for i in range(N):
    # i를 마지막으로 하는 수열을 만들려면,
    # i의 왼쪽에 있으면서 값이 더 작은 j만 고려 가능
    for j in range(i):
        if lst[j] < lst[i]:
            # j에서 i로 수열을 "이어붙이면" 길이는 dp[j] + 1
            # 더 긴 길이가 나오면 갱신
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 긴 증가 부분 수열의 "길이"는 dp 배열의 최댓값
print(max(dp))