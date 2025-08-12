T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # NxM 배열 입력
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 결과값 생성
    result = 0
    # 가장 자리 구역은 안전구역에서 제외하므로 (N-2)x(M-2) 범위만 탐색
    for i in range(1, N-1):
        for j in range(1, M-1):
            curr = matrix[i][j]     # 현재 좌표 기억
            cnt = 0                 # 안전구역인지 판별하기 위한 반환값 설정
            # 인접구역 델타 반복
            # 가장 자리 구역을 제외했기 때문에 ni, nj 범위 설정할 필요 없음
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = i + di, j + dj
                # 만약 인접구역이 더 높다면 -1 반환
                if matrix[ni][nj] > matrix[i][j]:
                    cnt = -1
            # 반환값이 -1이 아니라면 결과값 1 증가
            if cnt != -1:
                result += 1

    print(f'#{tc} {result}')
