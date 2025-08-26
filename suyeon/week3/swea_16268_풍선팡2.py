T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    stage = [list(map(int, input().split())) for _ in range(n)]

    direction = [[-1, 0], [1, 0], [0, -1],[0, 1]] #상하좌우

    max_balloon = 0
    for i in range(n):
        for j in range(m):
            balloon = 0
            balloon += stage[i][j]
            for dx, dy in direction:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < m:
                    balloon += stage[nx][ny]
            max_balloon = max(max_balloon, balloon)
    
    print(f'#{test_case} {max_balloon}')