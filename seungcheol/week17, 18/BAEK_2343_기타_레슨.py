import sys
input = sys.stdin.readline

N, M = map(int, input().split())
blue_lay = list(map(int, input().split()))

left = max(blue_lay)
right = sum(blue_lay)

while left <= right:
    mid = (left + right) // 2

    cnt = tmp = 0

    for i in blue_lay:
        if tmp + i <= mid:
            tmp += i
        else:
            tmp = i
            cnt += 1

    if cnt < M:
        right = mid - 1
    else:
        left = mid + 1

print(left)
