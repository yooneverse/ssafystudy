N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 첫 윈도우(앞에서 K개)의 합
window = 0
for i in range(K):
    window += arr[i]    # 첫 윈도우 합

max_sum = window

for j in range(K, N):
    window += arr[j] - arr[j - K]  # 오른쪽 값 추가, 왼쪽 값 제거
    if window > max_sum:
        max_sum = window

print(max_sum)
