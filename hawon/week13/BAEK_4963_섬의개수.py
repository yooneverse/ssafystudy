from collections import deque

delta_p = [[-1,0],[1,0],[0,-1],[0,1]]
delta_x = [[-1,-1],[-1,1],[1,-1],[1,1]]

def bfs(r,c):
    q = deque()
    q.append((r,c))
    # 만약에 대각선이나 상하좌우로 이어져있다면 섬임

    while q:
        qr, qc = q.popleft()
        for dr, dc in delta_p:
            nr = qr + dr
            nc = qc + dc
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and board[nr][nc] == 1:
                visited[nr][nc] = 1
                q.append((nr,nc))

        for dr, dc in delta_x:
            nr = qr + dr
            nc = qc + dc
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and board[nr][nc] == 1:
                visited[nr][nc] = 1
                q.append((nr,nc))

    return

while True:
    # 너비M, 높이N
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    board = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]

    island = 0

    # 출발점 찾기
    for r in range(N):
        for c in range(M):
            if board[r][c] == 1 and visited[r][c] == 0:
                visited[r][c] = 1
                bfs(r,c)
                island += 1

    print(island)