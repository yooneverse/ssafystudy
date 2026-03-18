from collections import deque

m, n, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()

# 처음부터 익은 토마토를 모두 큐에 넣기
for z in range(h):
    for x in range(n):
        for y in range(m):
            if board[z][x][y] == 1:
                q.append((z, x, y))

# 위, 아래, 앞, 뒤, 왼쪽, 오른쪽
dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]

while q:
    z, x, y = q.popleft()

    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
            if board[nz][nx][ny] == 0:
                board[nz][nx][ny] = board[z][x][y] + 1
                q.append((nz, nx, ny))

result = 0

for box in board:
    for row in box:
        for tomato in row:
            if tomato == 0:
                print(-1)
                exit()
        result = max(result, max(row))

print(result - 1)