N = int(input())
arr = list(map(int, input().split()))

# DP 배열 (모든 원소가 최소 자기 자신으로 길이 1의 부분수열 가능)
dp = [1] * N

# 각 원소를 기준으로 앞쪽 원소들과 비교
for i in range(1, N):
    for j in range(i):
        # 뒤에 있는 놈이 앞에 있는 놈보다 크면 (증가하면)
        if arr[j] < arr[i]:
            # 큰놈 추가시키기
            dp[i] = max(dp[i], dp[j] + 1)

# dp 리스트 중 최댓값
print(max(dp))