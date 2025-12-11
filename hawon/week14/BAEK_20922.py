N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = [0] * 100001

max_len = 0
left = 0

for right in range(N):
    x = arr[right]
    cnt[x] += 1

    while cnt[x] > K:
        cnt[arr[left]] -= 1
        left += 1

    now_len = right - left + 1

    if now_len > max_len:
        max_len = now_len

print(max_len)
