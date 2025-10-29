from collections import deque

drs = [-1,1,0,0]
dcs = [0,0,-1,1]

def atmos(r,c):
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((r,c))
    visited[r][c] = 1
    # 녹을 치즈 후보 저장
    cheese = []

    while q:
        sr,sc = q.popleft()
        for dr, dc in zip(drs,dcs):
            nr = sr + dr
            nc = sc + dc
            # 만약 범위를 벗어나지 않았고 방문하지 않았으면
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
                # 만약 주변 애들이 공기라면
                if board[nr][nc] == 0:
                    q.append((nr,nc))
                    visited[nr][nc] = 1
                # 치즈라면
                else:
                    cheese.append((nr,nc))
                    visited[nr][nc] = 1
    return cheese

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

time = 0
last = 0

while True:
    melted = atmos(0, 0)
    if not melted:  # 더 이상 녹을 치즈가 없으면
        print(time)
        print(last)
        break
    # 남은 치즈
    last = len(melted)
    for r, c in melted:
        board[r][c] = 0  # 치즈 녹이기
    time += 1