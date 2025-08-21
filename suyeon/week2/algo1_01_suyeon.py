# 문제 1: 김싸피의 고장난 스카우터

T = int(input())
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())  # n = 우주 크기, m = 스카우터 영역, k = 별 개수
    universe = [input() for _ in range(n)] # 문자열도 list와 동일하게 요소를 반복할 수 있으므로, 문자열 그대로 입력받았습니다.

    point_x = -1
    point_y = -1
    # 전체 우주 순회 후, 조건을 만족하는 영역이 없을 경우
    # -1, -1을 출력할 수 있도록 초기화 했습니다.

    # 우주순회
    for i in range(0, n - m + 1):
        # 스카우터가 탐색할 영역을 고려하여
        # 우주 전체 크기 - 스카우터 탐색 크기 + 1 (우주 끝까지 탐색해야하므로)
        # 예) n = 6이고, m = 3일 때 n - m = 3으로 스카우터 영역이 최대로 순회하는 영역은 (0, 0) ~ (4, 4)로 전체 우주를 순회하지 못합니다.
        for j in range(0, n - m + 1):
            num_star = 0
            # 스카우터 영역 순회
            for q in range(m):
                for s in range(m):
                    if universe[i + q][j + s] == '*':
                        num_star += 1

            # 스타우터 영역 순회가 다 끝나면, k와 동일한 개수의 *있는지 비교
            if num_star == k:
                # i, j를 기점으로 스카우터 영역을 탐색했으므로
                # k개의 별이 존재하는 영역의 첫 좌표도 i, j 입니다.
                point_x = i
                point_y = j
                break

        if point_x != -1 and point_y != -1:
            # 문제에서 조건을 만족하는 영역은 한 개 이하라고 했으므로,
            # 기본 point_x, point_y 값에서 바뀌면 필요없는 영역을 순회를 막기 위해 반복문을 종료합니다.
            # 위의 j 반복문 내에 break도 동일한 이유로 break를 넣었습니다.
            break

    print(f'#{test_case} {point_x} {point_y}')