import sys
input = sys.stdin.readline

def simulation():
    for _ in range(T):
        diffusion()
        air_purifier()
    total = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == -1:
                continue
            total += grid[i][j]
    return total

def diffusion():
    global grid
    tmp = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if grid[r][c] == -1 or not grid[r][c]:
                continue
            dust = grid[r][c]
            diff = dust // 5
            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                if nr >= R or nr < 0 or nc >= C or nc < 0:
                    continue
                if grid[nr][nc] == -1:
                    continue
                dust -= diff
                tmp[nr][nc] += diff
            tmp[r][c] += dust
    grid = tmp

def air_purifier():
    # 위쪽 순환
    for r in range(air[0] - 1, 0, -1):
        grid[r][0] = grid[r - 1][0]
    grid[0] = grid[0][1:] + [0]
    for r in range(0, air[0]):
        grid[r][C - 1] = grid[r + 1][C - 1]
    grid[air[0]] = [-1, 0] + grid[air[0]][1:C - 1]

    # 아래쪽 순환
    for r in range(air[1] + 1, R - 1):
        grid[r][0] = grid[r + 1][0]
    grid[R - 1] = grid[R - 1][1:] + [0]
    for r in range(R - 1, air[1], -1):
        grid[r][C - 1] = grid[r - 1][C - 1]
    grid[air[1]] = [-1, 0] + grid[air[1]][1:C - 1]

R, C, T = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(R)]

delta = ((1, 0), (0, 1), (-1, 0), (0, -1))

for r in range(R):
    if grid[r][0] == -1:
        air = (r, r + 1)
        break

print(simulation())
