from collections import deque

# 입력
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 방향 (상, 우, 하, 좌)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

answer = 0


def bfs():
    """현재 grid 상태에서 바이러스(2)를 퍼뜨린 뒤 안전영역(0) 개수를 계산"""
    vmap = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            vmap[i][j] = grid[i][j]

    q = deque()

    # 바이러스 시작점 추가
    for i in range(N):
        for j in range(M):
            if vmap[i][j] == 2:
                q.append((i, j))

    # 바이러스 확산
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if vmap[nr][nc] == 0:
                    vmap[nr][nc] = 2
                    q.append((nr, nc))

    # 안전영역 계산
    safe = 0
    for i in range(N):
        for j in range(M):
            if vmap[i][j] == 0:
                safe += 1

    global answer
    if safe > answer:
        answer = safe


def dfs(depth):
    """벽 3개를 세우는 모든 경우 탐색"""
    if depth == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                grid[i][j] = 1
                dfs(depth + 1)
                grid[i][j] = 0


# 실행
dfs(0)
print(answer)
