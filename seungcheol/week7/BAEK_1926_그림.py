# bfs
from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(y, x):
    q = deque([(y, x)])
    dist = 0

    while q:
        r, c = q.popleft()

        if visited[r][c]:
            continue
        visited[r][c] = 1
        dist += 1

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if visited[nr][nc]:
                continue
            if matrix[nr][nc]:
                q.append((nr, nc))

    return dist

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

area = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        if matrix[i][j]:
            cnt += 1
            tmp = bfs(i, j)
            area = max(area, tmp)

print(cnt)
print(area)