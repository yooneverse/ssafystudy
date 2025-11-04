from collections import deque

def bfs(r, c):
    que = deque([(r, c)])

    while que:
        r, c = que.popleft()

        for dr, dc in delta:
            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                continue
            if grid[nr][nc] and not visited[nr][nc]:
                que.append((nr, nc))
                visited[nr][nc] = 1
    return

delta = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break

    grid = [list(map(int, input().split())) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]
    answer = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] and not visited[i][j]:
                visited[i][j] = 1
                bfs(i, j)
                answer += 1

    print(answer)
