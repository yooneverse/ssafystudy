# BAEK 3055. 탈출
import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())

# '.': 비어있는 곳
# '*': 물이 차있는 지역
# 'X': 돌
# 'D': 비버의 굴
# 'S': 고슴도치의 위치

# 매 분마다 고슴도치는 인접한 네 칸 중 하나로 이동 가능
# 물도 매 분마다 비어있는 칸으로 확장
# 물과 고슴도치는 돌을 통과할 수 없음
# 고슴도치는 물로 차있는 구역으로 이동 불가
# 물도 비버의 소굴로 이동 불가

# 고슴도치가 안전하게 비버의 굴로 이동하기 위한 최소 시간 구하기
# 물이 찰 예정인 칸으로 이동 불가

grid = [list(input().strip()) for _ in range(R)]

d = (-1, 0), (1, 0), (0, -1), (0, 1)

water = deque()
dochi = deque()
visited = set()

for i in range(R):
    for j in range(C):
        if grid[i][j] == '*':
            water.append((i, j))
        elif grid[i][j] == 'D':
            biber = (i, j)
        elif grid[i][j] == 'S':
            dochi.append((i, j, 0))
            grid[i][j] = '.'
            visited.add((i, j))

best = float('inf')

# 물부터 채움
while dochi:
    K = len(water)
    for _ in range(K):
        i, j = water.popleft()
        for di, dj in d:
            ni, nj = di + i, dj + j
            if ni < 0 or ni >= R or nj < 0 or nj >= C:
                continue
            if grid[ni][nj] == '.':
                water.append((ni, nj))
                grid[ni][nj] = '*'

    K = len(dochi)
    for _ in range(K):
        y, x, time = dochi.popleft()
        for dy, dx in d:
            ny, nx = dy + y, dx + x
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            if grid[ny][nx] in ('*', 'X'):
                continue
            if grid[ny][nx] == 'D':
                best = min(best, time + 1)
                continue
            if (ny, nx) not in visited:
                visited.add((ny, nx))
                dochi.append((ny, nx, time + 1))

if best != float('inf'):
    print(best)
else:
    print('KAKTUS')
