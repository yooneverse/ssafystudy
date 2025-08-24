# 0, 통로, 1 = 벽, 2 = 출발지, 3 = 도착지
MAZE_SIZE = 100
T = 10


def find_start_end(arr):
    s = e = 0
    for x in range(MAZE_SIZE):
        for y in range(MAZE_SIZE):
            if arr[x][y] == '2':
                s = (x, y)
            elif arr[x][y] == '3':
                e = (x, y)
    return s, e


def BFS(arr, s_xy):
    queue = []
    visited = [[0] * MAZE_SIZE for _ in range(MAZE_SIZE)]

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    queue.append(s_xy)
    visited[s_xy[0]][s_xy[1]] = 1
    while queue:
        now = queue.pop(0)

        for dx, dy in direction:
            nx = now[0] + dx
            ny = now[1] + dy
            if 0 <= nx < MAZE_SIZE and 0 <= ny < MAZE_SIZE:
                if not visited[nx][ny] and arr[nx][ny] == '0':
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[now[0]][now[1]] + 1
                elif arr[nx][ny] == '3':
                    visited[nx][ny] = visited[now[0]][now[1]] + 1
                    return 1
    return 0


for test_case in range(1, T + 1):
    test_num = int(input())
    maze = [input() for _ in range(MAZE_SIZE)]

    start, end = find_start_end(maze)

    print(f'#{test_case} {BFS(maze, start)}')