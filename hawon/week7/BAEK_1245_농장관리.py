from collections import deque

# 8방향 (상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
dr = [-1, 1, 0, 0, -1, -1,  1, 1]
dc = [ 0, 0,-1, 1, -1,  1, -1, 1]

def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = 1
    h = grid[sr][sc]         # 현재 높이
    is_peak = True           # 일단 봉우리라고 가정하고 시작

    while q:
        r, c = q.popleft()

        for k in range(8):
            nr, nc = r + dr[k], c + dc[k]

            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 더 높은 칸이 인접해 있다면 봉우리가 아님
            if grid[nr][nc] > h:
                is_peak = False

            # 같은 높이인데 아직 방문 안 했다면 -> 같은 영역
            if grid[nr][nc] == h and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))

    # 전체를 다 돌고 난 후
    # 더 높은 칸이 한 번도 없었다면 진짜 봉우리
    return is_peak


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

ans = 0

for r in range(N):
    for c in range(M):
        # 이미 방문했거나, 높이가 0이면 탐색 안 함
        if visited[r][c] or grid[r][c] == 0:
            continue

        if bfs(r, c):
            ans += 1

print(ans)