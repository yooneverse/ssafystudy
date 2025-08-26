# 중심을 기준으로 주변 8개 구역 탐색
# 조건 1: 중심보다 높이가 낮은 방향만 촬영 가능
# 조건 2: 예비 후보지는 사진을 찍을 수 있는 방향이 4방향 이상
# 조건 3: 높이 정보가 없는 영역이 있어도, 조건 2만 맞으면 후보지 가능
# 출력: 예비 후보지 수

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    section = [list(map(int, input().split())) for _ in range(n)]

    direction = [[-1, -1], [-1, 0], [-1, 1],
                 [0, -1], [0, 1],
                 [1, -1], [1, 0], [1, 1]]
    
    spare = 0
    for i in range(n):
        for j in range(m):
            cnt = 0
            landing = section[i][j]
            for dx, dy in direction:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if section[nx][ny] < landing:
                        cnt += 1
            if cnt >= 4:
                spare += 1
    
    print(f'#{test_case} {spare}')