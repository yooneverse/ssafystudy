def find_start_end(graph, graph_size):
    s = e = 0
    for i in range(graph_size):
        for j in range(graph_size):
            if graph[i][j] == '3':
                e = (i, j)
            elif graph[i][j] == '2':
                s = (i, j)
    return s, e  # ((start), (end)) 형태로 출력될 거임


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    # maze = [list(map(int, input().split('')))]
    maze = [input() for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    queue = []

    # 시작점과 종료점 찾기
    start, end = find_start_end(maze, n)

    # 방향 정의
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우

    # 처음 방향 visited
    visited[start[0]][start[1]] = 1
    queue.append(start)
    is_route = False
    while queue:
        now = queue.pop(0)

        for dx, dy in direction:  # now 기준으로 갈 수 있는 곳 다 찾고, queue에 삽입
            nx = now[0] + dx
            ny = now[1] + dy
            if 0 <= nx < n and 0 <= ny < n:
                if maze[nx][ny] == '0' and not visited[nx][ny]:  # 갈 수 있는 모든 방향 큐에 입력
                    visited[nx][ny] = visited[now[0]][now[1]] + 1  # start 기준으로 거리 계산
                    queue.append((nx, ny))
                elif maze[nx][ny] == '3':
                    visited[nx][ny] = visited[now[0]][now[1]] + 1  # start 기준으로 거리 계산
                    queue.append((nx, ny))
                    is_route = True
                    break

        if is_route:
            break

    if not is_route:
        print(f'#{test_case} 0')  # 시작점, 종점 빼기
    else:
        print(f'#{test_case} {visited[end[0]][end[1]] - 2}')  # 시작점, 종점 빼기