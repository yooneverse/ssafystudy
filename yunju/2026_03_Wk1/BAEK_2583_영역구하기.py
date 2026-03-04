'''
빈 영역 찾기

점을 주어져서 선분을 이용해야 할 것 같았지만
직사각형을 이용

존재하는 직사각형을 색칠하고 빈 공간을
덱을 이용해서 파악
'''

import sys
from collections import deque
input_data = sys.stdin.read().split()

M, N, K = map(int, input_data[:3])
rects = input_data[3:]

grid = [[0] * N for _ in range(M)]

idx = 0
for _ in range(K):
    x1, y1, x2, y2 = map(int, rects[idx:idx+4])
    # 주어진 좌표 범위의 직사각형을 1로 색칠
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1
    idx += 4

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

areas = []

for i in range(M):
    for j in range(N):
        # 색칠되지 않은 빈 공간(0)을 발견 시 BFS 탐색 시작
        if grid[i][j] == 0:  
            queue = deque([(i, j)])
            grid[i][j] = 1  
            count = 1
            
            while queue:
                y, x = queue.popleft()
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < M and 0 <= nx < N and grid[ny][nx] == 0:
                        grid[ny][nx] = 1
                        count += 1
                        queue.append((ny, nx))
            
            areas.append(count)

print(len(areas))
print(*(sorted(areas)))