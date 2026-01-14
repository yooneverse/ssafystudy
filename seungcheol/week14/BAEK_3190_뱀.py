import sys
input = sys.stdin.readline

from collections import deque

def check(r, c):
    return 0 <= r < N and 0 <= c < N

def snake():
    q = deque([(0, 0)])
    direction = 0
    cnt = 0
    for time, rotate in control:
        while cnt < time:
            cnt += 1
            r, c = q[-1]
            dr, dc = delta[direction]
            nr = r + dr
            nc = c + dc
            if not check(nr, nc):
                return cnt
            if grid[nr][nc] == 2:
                return cnt
            elif grid[nr][nc] == 1:
                q.append((nr, nc))
                grid[nr][nc] = 2
            else:
                q.append((nr, nc))
                grid[nr][nc] = 2
                xr, xc = q.popleft()
                grid[xr][xc] = 0
        if rotate == 'L':
            direction = (direction + 3) % 4
        else:
            direction = (direction + 1) % 4
    while True:
        cnt += 1
        r, c = q[-1]
        dr, dc = delta[direction]
        nr = r + dr
        nc = c + dc
        if not check(nr, nc):
            return cnt
        if grid[nr][nc] == 2:
            return cnt
        elif grid[nr][nc] == 1:
            q.append((nr, nc))
            grid[nr][nc] = 2
        else:
            q.append((nr, nc))
            grid[nr][nc] = 2
            xr, xc = q.popleft()
            grid[xr][xc] = 0
    return cnt

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

N = int(input().strip())
K = int(input().strip())
grid = [[0] * N for _ in range(N)]
grid[0][0] = 2

for _ in range(K):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = 1

L = int(input().strip())

control = [0] * L
for idx in range(L):
    X, C = input().split()
    T = int(X)
    control[idx] = (T, C)

answer = snake()

print(answer)
