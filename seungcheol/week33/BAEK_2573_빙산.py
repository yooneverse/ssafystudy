import sys
input = sys.stdin.readline

from collections import deque

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

def solve():
    ice = deque([])
    for row in range(1, r - 1):
        for col in range(1, c - 1):
            if not grid[row][col]:
                continue
            water = 0
            for dr, dc in delta:
                nr, nc = row + dr, col + dc
                if grid[nr][nc]:
                    continue
                water += 1
            ice.append((water, row, col))

    year = 0

    while ice:
        visited = [[0] * c for _ in range(r)]

        berg = 0

        for _, row, col in ice:
            if visited[row][col]:
                continue
            visited[row][col] = 1
            berg += 1
            if berg > 1:
                return year
            que = deque([(row, col)])
            while que:
                ir, ic = que.popleft()

                for dr, dc in delta:
                    nr, nc = ir + dr, ic + dc
                    if visited[nr][nc]:
                        continue
                    if not grid[nr][nc]:
                        continue
                    que.append((nr, nc))
                    visited[nr][nc] = 1

        for _ in range(len(ice)):
            water, row, col = ice.popleft()
            if water >= grid[row][col]:
                grid[row][col] = 0
            else:
                grid[row][col] -= water
                ice.append((water, row, col))

        for _ in range(len(ice)):
            tmp, row, col = ice.popleft()

            water = 0
            for dr, dc in delta:
                nr, nc = row + dr, col + dc
                if grid[nr][nc]:
                    continue
                water += 1
            ice.append((water, row, col))

        year += 1
    return 0

r, c = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(r)]

answer = solve()

print(answer)
