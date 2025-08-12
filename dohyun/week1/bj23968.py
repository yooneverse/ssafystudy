N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0     # 반복 횟수 초기 설정

for last in range(N-1, 0, -1):  # 정렬할 구간의 끝 설정
    for i in range(last):       # 왼쪽 원소의 인덱스
        # 왼쪽이 크면 오른쪽 원소와 교환
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
            cnt += 1    # 반복 횟수 + 1
            if cnt == K:    # 반복 횟수가 K에 다다르면
                print(f'{A[i]} {A[i + 1]}')

if cnt < K:   # 반복 횟수가 K보다 작으면
    A = [-1]  # -1 출력
    print(*A)
