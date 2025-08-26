T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(n)]

    direction_plus = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    direction_x = [[-1, -1],[-1, 1], [1, -1], [1, 1]]


    max_kill = 0
    for i in range(n):
        for j in range(n):
            kill_plus = 0
            kill_x = 0

            kill_plus += flies[i][j]
            for dx, dy in direction_plus:
                for k in range(1, m): # 중심 포함 안하고 m - 1칸 분사
                    nx = i + (dx * k)
                    ny = j + (dy * k)
                    if 0 <= nx < n and 0 <= ny < n:
                        kill_plus += flies[nx][ny]

            kill_x += flies[i][j]
            for dx, dy in direction_x:
                for k in range(1, m): # 중심 포함 안하고 m - 1칸 분사
                    nx = i + (dx * k)
                    ny = j + (dy * k)
                    if 0 <= nx < n and 0 <= ny < n:
                        kill_x += flies[nx][ny]
            
            max_kill = max(max_kill, kill_plus, kill_x)

    print(f'#{test_case} {max_kill}')