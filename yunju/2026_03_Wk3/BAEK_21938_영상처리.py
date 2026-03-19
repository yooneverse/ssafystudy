'''
세로 N 가로 M 픽셀
색상은 0~255

세가지색 평균
경계값 T보다 크거나 같으면 255
작으면 0

255는 물체. 인접 시 같은 물체

총 몇 개 물체?
'''

import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int, input().split())
display = []
for _ in range(N):
    line = list(map(int, input().split()))
    row = []
    for i in range(0, len(line), 3):
        avg = (line[i]+line[i+1]+line[i+2]) / 3
        row.append(avg)
    display.append(row)

T = int(input())
for i in range(N):
    for j in range(M):
        if display[i][j] >= T:
            display[i][j] = 255
        else:
            display[i][j] = 0

visited = [[False]*M for _ in range(N)]
count = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
    
for i in range(N):
    for j in range(M):
        if display[i][j] == 255 and not visited[i][j]:
            count += 1
            queue = deque([(i, j)])
            visited[i][j] = True
                
            while queue:
                r, c = queue.popleft()
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if not visited[nr][nc] and display[nr][nc] == 255:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
print(count)