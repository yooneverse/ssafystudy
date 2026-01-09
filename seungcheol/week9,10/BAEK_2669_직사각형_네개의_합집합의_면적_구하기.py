import sys
input = sys.stdin.readline

grid = [[0] * 101 for _ in range(101)]
answer = 0

for _ in range(4):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(lx, rx):
        for j in range(ly, ry):
            if grid[i][j]:
                continue
            answer += 1
            grid[i][j] = 1

print(answer)
