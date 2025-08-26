def BFS(arr, visit_arr, que):
    while que:
        now = que.pop(0)
        for dy, dx in direction:
            ny = now[0] + dy
            nx = now[1] + dx
            if 0 <= ny < n and 0 <= nx < m and farm[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = 1
                que.append((ny,nx))


T = int(input())
for test_case in range(1, T + 1):

    # 배추 심을 밭 구하기
    # m = 배추밭 가로 길이(열), n = 세로 길이(행), k = 배추 개수
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]

    # 밭에 배추 심기
    for _ in range(k):
        # x = 열, y = 행
        x, y = map(int, input().split())
        farm[y][x] = 1
    

    # 지렁이한테 보호받을 수 있는 배추 군집 구하기
    # 지렁이는 상,하,좌,우로 움직일 수 있고
    # 상, 하, 좌, 우에 이어져 있으면 다~ 갈 수 있으므로 연결되어 있는 군집을 찾는 것
    # 즉 군집 개수 = 지렁이 개수
    direction = [[-1,0],[1,0],[0,-1],[0,1]] # 상하좌우
    visited = [[0] * m for _ in range(n)]
    q = []
    worm = 0
    
    # 밭 돌아다니면서 배추 모여있는 곳 찾기
    for iy in range(n):
        for jx in range(m):
            if farm[iy][jx] == 1 and not visited[iy][jx]:
                visited[iy][jx] = 1 # 첫 시작점 방문 표시
                q.append((iy,jx)) # 시작점 q 삽입
                BFS(farm, visited, q) # 시작점을 기준으로 근처에 있는 배추 찾기
                worm += 1 # 연결되어 있는 모든 배추를 찾으면 여기는 벌레로 커버 가능
    print(worm)


