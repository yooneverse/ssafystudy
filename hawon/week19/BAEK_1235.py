import sys
input = sys.stdin.readline

n = int(input().strip())

nums = []
for _ in range(n):
    nums.append(input().strip())

L = len(nums[0])


for k in range(1, L + 1):
    seen = set()
    for i in range(n):
        suffix = nums[i][L - k:]
        seen.add(suffix)

    if len(seen) == n:
        print(k)
        break