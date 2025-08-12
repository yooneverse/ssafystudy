T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # NxN 배열 입력
    matrix = [list(map(str, input())) for _ in range(N)]
    # 별의 개수합이 K개인 영역이 없을 경우 출력될 결과값 설정
    result = [-1, -1]
    # (0, 0) 부터 MxM 영역이 닿는 곳{(N-M)x(N-M)}까지 범위 설정
    for i in range(N-M+1):
        for j in range(N-M+1):
            curr = matrix[i][j]     # 현재 좌표 기억
            star_sum = 0            # 별의 개수합 0으로 초기화
            # MxM 영역으로 탐색
            for a in range(M):
                for b in range(M):
                    # 별을 찾으면 별의 개수합 1 증가
                    if matrix[i+a][j+b] == '*':
                        star_sum += 1
            # 별의 개수합이 K이면 결과값으로 현재 좌표 대입
            if star_sum == K:
                result = [i, j]

    print(f'#{tc} {" ".join(map(str, result))}')
