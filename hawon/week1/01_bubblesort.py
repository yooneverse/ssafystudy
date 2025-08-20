N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0  # 교환 횟수

# 버블 정렬
for i in range(N - 1, 0, -1):
    for j in range(i):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            count += 1
            if count == K:
                print(*A)
if count < K:
    print(-1)