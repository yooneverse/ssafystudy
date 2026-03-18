import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lines = list(int(input().strip()) for _ in range(k))

left = 1
right = max(lines)
answer = 0

while left <= right:
    check = 0

    mid = (left + right) // 2
    for line in lines:
        check += line // mid

    if check < n:
        right = mid - 1
    else:
        answer = mid
        left = mid + 1

print(answer)
