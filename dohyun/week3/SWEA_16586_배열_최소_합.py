# 16586. 5일차 - 배열 최소 합
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 초기 비교 대상을 matrix 의 대각선 방향 값으로 잡는다.
    min_sum = 0
    for n in range(N):
        min_sum += matrix[n][n]
    # 행의 위치를 배열로 설정
    # ex) N = 3, row = [0, 1, 2] -> idx(열 정보)와 연계하여 사용
    # ex2) idx = 1 -> row[idx] = 1 => (1, 1) 나타냄
    row = list(range(N))

    # 순열 생성 + 백트래킹 함수
    def back_track(idx, sum_num):
        # 전역 변수 선언
        global min_sum
        # 재귀 횟수가 N에 다다르면 2차원 배열 값의 합과 전역 변수 비교
        # 그 후 재귀 중단
        if idx == N:
            if min_sum > sum_num:
                min_sum = sum_num
                return
        # 재귀 중 전역 변수보다 2차원 배열 값의 합이 커지면 재귀 중단
        if min_sum <= sum_num:
            return

        # 순열 생성하기 위해 행 번호가 저장된 row 배열의 값을 바꾸며 재귀 작동
        # ex) [0, 1, 2] -> [0, 2, 1]
        # -> [0, 1, 2](원상복구) -> [1, 0, 2] -> [1, 2, 0] -> ...
        # 순열에 따라 idx 열의 row[idx] 행 값을 sum_num 에 저장
        for c in range(idx, N):
            row[idx], row[c] = row[c], row[idx]
            back_track(idx + 1, sum_num + matrix[row[idx]][idx])
            # 재귀 중단 후 col 원상 복구
            row[idx], row[c] = row[c], row[idx]

    back_track(0, 0)
    print(f'#{tc} {min_sum}')
