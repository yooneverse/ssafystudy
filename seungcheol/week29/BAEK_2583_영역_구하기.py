import sys
input = sys.stdin.readline


from collections import deque

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

def bfs(row, col):
    count = 1
    grid[row][col] = 2
    que = deque([(row, col)])

    while que:
        r, c = que.popleft()

        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and not grid[nr][nc]:
                grid[nr][nc] = 2
                que.append((nr, nc))
                count += 1
    return count


m, n, k = map(int, input().split())

grid = [[0] * n for _ in range(m)]

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for y in range(ly, ry):
        for x in range(lx, rx):
            grid[y][x] = 1

answer = []
for r in range(m):
    for c in range(n):
        if not grid[r][c]:
            answer.append(bfs(r, c))

answer.sort()
print(len(answer))
print(*answer)
