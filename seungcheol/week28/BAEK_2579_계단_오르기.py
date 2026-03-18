import sys
input = sys.stdin.readline

n = int(input().strip())
nums = []

for _ in range(n):
    num = int(input().strip())
    nums.append(num)

if n <= 2:
    answer = sum(nums)
else:
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = nums[0] + nums[1]

    for i in range(2, n):
        dp[i] = max(dp[i - 3] + nums[i - 1] + nums[i], dp[i - 2] + nums[i])

    answer = dp[n - 1]

print(answer)
