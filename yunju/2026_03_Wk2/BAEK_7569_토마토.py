'''
토마토
3차원 bfs
덱을 이용해서 퍼져나감

익은 토마토로부터 퍼져나감

모든 토마토가 다 익을 수 있는가? 그렇다면 최소 일수는?
'''

from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque()
zero = 0

for level in range(H):
    for row in range(N):
        for col in range(M):
            # 익은 토마토
            if boxes[level][row][col] == 1:
                q.append((level, row, col))
            # 안 익은 토마토
            elif boxes[level][row][col] == 0:
                zero += 1

# 3차원에서는 여섯 방향으로 이동 가능함
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while q:
    z, x, y = q.popleft()
    for d in range(6):
        nz, nx, ny = z+dz[d], x+dx[d], y+dy[d]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
            if boxes[nz][nx][ny] == 0:
                boxes[nz][nx][ny] = boxes[z][x][y] + 1
                q.append((nz, nx, ny))

max_day = 0
for level in range(H):
    for row in range(N):
        for col in range(M):
            if boxes[level][row][col] == 0:
                print(-1)
                # 함수였으면 return하는 건데 함수로 안 만들어서 sys.exit() 사용
                sys.exit()
            max_day = max(max_day, boxes[level][row][col])

print(max_day - 1)
