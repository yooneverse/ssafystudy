import sys

input = sys.stdin.readline

from collections import deque

sys.setrecursionlimit(100000)

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

n = int(input().strip())

grid = [list(input().strip()) for _ in range(n)]

weakness = healthy = 0

visit_w = [list(0 for _ in range(n)) for _ in range(n)]
visit_h = [list(0 for _ in range(n)) for _ in range(n)]


def check(row, col):
    return 0 <= row < n and 0 <= col < n


def dfs(row, col, color):
    visit_h[row][col] = 1
    for dr, dc in delta:
        nr, nc = row + dr, col + dc
        if not check(nr, nc):
            continue
        if visit_h[nr][nc]:
            continue
        if color == grid[nr][nc]:
            dfs(nr, nc, color)


def bfs(row, col, color):
    que = deque([(row, col)])
    visit_w[row][col] = 1

    while que:
        r, c = que.popleft()

        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if not check(nr, nc):
                continue
            if visit_w[nr][nc]:
                continue
            if color == grid[nr][nc] == "B":
                visit_w[nr][nc] = 1
                que.append((nr, nc))
            elif color in ("R", "G") and grid[nr][nc] in ("R", "G"):
                visit_w[nr][nc] = 1
                que.append((nr, nc))


for r in range(n):
    for c in range(n):
        if not visit_h[r][c]:
            dfs(r, c, grid[r][c])
            healthy += 1
        if not visit_w[r][c]:
            bfs(r, c, grid[r][c])
            weakness += 1

print(healthy, weakness)
