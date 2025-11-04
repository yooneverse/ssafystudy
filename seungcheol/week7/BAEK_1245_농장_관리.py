from collections import deque

def mountain(start):
    global answer

    que = deque([start])
    flag = True

    while que:
        r, c = que.popleft()

        if visited[r][c]:
            continue
        visited[r][c] = 1

        for dr, dc in delta:
            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if grid[r][c] == grid[nr][nc]:
                que.append((nr, nc))
            elif grid[r][c] < grid[nr][nc]:
                flag = False
    if flag:
        answer += 1


N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

visited = [[0] * M for _ in range(N)]

answer = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            mountain((i, j))

print(answer)