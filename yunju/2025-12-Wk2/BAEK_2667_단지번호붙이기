'''
정사각형 지도
연결된 집

단지의 총 개수와 단지별 집의 개수 오름차순 정렬
'''

import sys
input = sys.stdin.readline
from collections import deque

def solve(x,y):
    cnt = 1
    q = deque()
    q.append((x,y))


    while q:
        cx,cy = q.popleft()
        for (dx, dy) in ((0,1),(0,-1),(1,0),(-1,0)):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny] == '1':
                    if not visited[nx][ny]:
                        cnt += 1
                        visited[nx][ny] = 1
                        q.append((nx,ny))

    villages.append(cnt)

N = int(input())
board = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
villages = []

for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            if not visited[i][j]:
                visited[i][j] = 1
                solve(i,j)
print(len(villages))
villages.sort()
for i in villages:
    print(i)