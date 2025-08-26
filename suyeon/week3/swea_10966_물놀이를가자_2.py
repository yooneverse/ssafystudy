def find_water(arr, row, col):
    idx_xy = []
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 'W':
                idx_xy.append((i, j))
    return idx_xy


def BFS(arr, s):
    global n, m
    q = s
    visited = [[0] * m for _ in range(n)]

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우

    while q:
        now = q.pop(0)

        for dx, dy in direction:  # now 기준으로 갈 수 있는 곳 다 찾고, queue에 삽입
            nx = now[0] + dx
            ny = now[1] + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and arr[nx][ny] == 'L':
                    visited[nx][ny] = visited[now[0]][now[1]] + 1
                    q.append((nx, ny))
    return visited

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [input() for _ in range(n)]

    start = find_water(graph, n, m)
    
    distance = BFS(graph, start)

    result = sum(map(sum,distance))

    print(f'#{test_case} {result}')
