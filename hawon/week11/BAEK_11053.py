N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        # 뒤에 있는 놈이 앞에 있는 놈보다 크면 (증가하면)
        if arr[j] < arr[i]:
            # 큰놈 추가시키기
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

"""
arr = [10, 20, 10, 30, 20, 50]
"""