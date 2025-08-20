# 문제 2: 강우 안전구역

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    section = [list(map(int, input().split())) for _ in range(n)]

    safe_section = 0
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상/하/좌/우

    for i in range(1, n - 1): # 인접구역 정보가 부족한 첫 행과 마지막 행 제외
        for j in range(1, m - 1): # 인접구역 정보가 부족한 첫 열과 마지막 열 제외
            max_section = 0
            for dx, dy in direction: # 상하좌우 인접구역 간의 최대값 찾기
                nx = i + dx
                ny = j + dy
                if max_section < section[nx][ny]:
                    # 첫 행, 마지막 행, 첫 열, 마지막 열 이외에 배열 탐색을 하므로
                    # 배열의 크기를 벗어날 일이 없으므로 위치가 올바른 위치인지 비교 하지 않고
                    # 바로 최대값 비교를 합니다.
                    max_section = section[nx][ny]

            if max_section < section[i][j]:
                # 인접구역 내의 최대값과 중심값 비교
                # 중심값이 더 클 경우 = 모든 인접구역보다 높은 지역 = 안전구역
                safe_section += 1

    print(f'#{test_case} {safe_section}')