def BFS(arr, s):
    global n, m
    q = []
    visited = [[0] * m for _ in range(n)]

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우

    q.append(s)
    visited[s[0]][s[1]] = 0
    while q:
        now = q.pop(0)

        for dx, dy in direction:  # now 기준으로 갈 수 있는 곳 다 찾고, queue에 삽입
            nx = now[0] + dx
            ny = now[1] + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[now[0]][now[1]] + 1
                    q.append((nx, ny))
                    if arr[nx][ny] == 'W':
                        return visited[nx][ny]
    return -1


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [input() for _ in range(n)]

    min_sum = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'W':
                continue
            else:
                start = (i, j)
                distance = BFS(graph, start)
                min_sum += distance

    print(f'#{test_case} {min_sum}')
