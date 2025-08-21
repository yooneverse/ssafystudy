N, K = map(int, input().split())  
A = list(map(int, input().split()))  
count = 0  # 교환 횟수 초기화

# 버블 정렬 수행
for last in range(N - 1, 0, -1):
    for i in range(last):
        if A[i] > A[i + 1]:
            # 교환 발생
            A[i], A[i + 1] = A[i + 1], A[i]
            count += 1

            # K번째 교환 직후 상태 출력
            if count == K:
                print(' '.join(map(str, A)))
                # K번째 교환 후 출력이 되었으면 더 이상 진행할 필요 없으므로 break
                break
    # K번째 교환을 완료했다면, 바깥쪽 for문도 종료
    if count == K:
        break

# 교환 횟수가 K에 미치지 못하면 -1 출력
if count < K:
    print(-1)