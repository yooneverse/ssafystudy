def road_length(start_x, start_y):
    global n, mountain
    direction = (-1, 0), (1, 0), (0, -1), (0, 1)
    lowest = (start_x, start_y)
    # 반복문을 다 돌면 시작점을 기준으로 가장 낮은 지대로 이동할 것
    for dx, dy in direction:
        nx = start_x + dx
        ny = start_y + dy
        if 0 <= nx < n and 0 <= ny < n and mountain[lowest[0]][lowest[1]] > mountain[nx][ny]:
            lowest = (nx, ny)

    # 가장 낮은 지대가 시작점과 같으면 재귀 멈춤
    if start_x == lowest[0] and start_y == lowest[1]:
        return 1
    else:
        return 1 + road_length(lowest[0], lowest[1])


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    mountain = [list(map(int, input().split())) for _ in range(n)]

    longest = 0
    # 산 등산 시작
    for i in range(n):
        for j in range(n):
            # 첫 시작점을 기점으로 등산로 찾기
            length = road_length(i, j)

            if longest < length:
                longest = length

    print(f'#{test_case} {longest}')