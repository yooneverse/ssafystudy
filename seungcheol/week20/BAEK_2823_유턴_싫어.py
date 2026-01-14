import sys
input = sys.stdin.readline

r, c = map(int, input().split())

grid = [input().strip() for _ in range(r)]

delta = ((-1, 0), (0, -1), (1, 0), (0, 1))

answer = 0
for i in range(r):
    for j in range(c):
        path = 0
        if grid[i][j] == '.':
            for di, dj in delta:
                ni, nj = i + di, j + dj
                if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == '.':
                    path += 1
            if path <= 1:
                answer = 1
print(answer)