# Todo : 섬 개수 세기
# 0과 1로 이루어져 있고, 1이 이어지는 걸 세면 됨(상하좌우 대각선)

# 상하좌우 대각선
drs = [-1,1,0,0,1,1,-1,-1]
dcs = [0,0,-1,1,1,-1,1,-1]

def dfs(r,c):
    visited[r][c] = 1
    for dr, dc in zip(drs,dcs):
        nr = r + dr
        nc = c + dc
        if 0<=nr<N and 0<=nc<M:
            if not visited[nr][nc] and grid[nr][nc] == 1:
                dfs(nr,nc)

# 맨 마지막 줄에 0 0 들어오기 전까지 입력 받기
while True:
    # 너비, 높이
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break

    # 지도
    grid = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]

    cnt = 0

    for r in range(N):
        for c in range(M):
            if grid[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                cnt += 1
    print(cnt)