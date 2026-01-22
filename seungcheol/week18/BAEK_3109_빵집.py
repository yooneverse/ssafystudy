import sys
input = sys.stdin.readline

r, c = map(int, input().split())

grid = [list(input().strip()) for _ in range(r)]

delta = ((-1, 1), (0, 1), (1, 1))

def dfs(row, col):
    if col == c - 1:
        return 1
    
    for dr, dc in delta:
        nr, nc = row + dr, col + dc

        if 0 <= nr < r and 0 <= nc < c and grid[nr][nc] == '.':
            grid[nr][nc] = 'X'
            if dfs(nr, nc):
                return 1
    return 0

answer = 0
for i in range(r):
    if grid[i][0] == '.':
        grid[i][0] = 'X'
        answer += dfs(i, 0)

print(answer)
