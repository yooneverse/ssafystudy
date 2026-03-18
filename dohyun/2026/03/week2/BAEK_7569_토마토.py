# BAEK 7569. 토마토
import sys
from collections import deque
input = sys.stdin.readline


# 상하좌우앞뒤 토마토가 익는다
M, N, H = map(int, input().split())

matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# print(matrix)
# print(matrix[0][1][2])
# 인덱스 별로 +-1을 한 값이 범위 내이고, 토마토라면 익힌다.
q = deque()
d = (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 1:
                q.append((i, j, k, 0))

complete = 0

while q:
    h, r, c, day = q.popleft()
    for dh, dr, dc in d:
        nh, nr, nc = dh + h, dr + r, dc + c
        if nh < 0 or nh >= H or nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if matrix[nh][nr][nc] == 0:
            matrix[nh][nr][nc] = 1
            complete = max(complete, day + 1)
            q.append((nh, nr, nc, day + 1))

ok = False

for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 0:
                print(-1)
                ok = False
                break
        else:
            ok = True
        
        if not ok:
            break
    else:
        ok = True
    
    if not ok:
        break
else:
    print(complete)