N = int(input())
target = int(input())

grid = [[0] * N for _ in range(N)]

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
num = dist = 1
cnt = dirs = line = 0
row = col = N // 2
answer = None
while num <= N ** 2:
    if num == target:
        answer = (row + 1, col + 1)
    grid[row][col] = num
    num += 1
    if line < dist:
        dr, dc = delta[dirs]
        row += dr
        col += dc
        line += 1
    else:
        line = 1
        dirs = (dirs + 1) % 4
        dr, dc = delta[dirs]
        row += dr
        col += dc
        cnt += 1
    if cnt == 2:
        cnt = 0
        dist += 1

for i in range(N):
    print(*grid[i])
print(*answer)
