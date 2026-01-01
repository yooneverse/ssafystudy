'''
특정 높이 이하 물에 잠김
물에 잠기지 않는 영역의 최대 개수
'''
'''
덱을 이용
연결된 물에 잠기지 않은 지역을 하나로 카운트
'''


import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 시작 지점 (x,y)
# 높이별로 남은 영역의 개수를 계산하므로 visited를 따로 사용함
def bfs(x,y,height, visited, n, graph):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<= nx < n and 0<= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > height:
                    visited[nx][ny] = True
                    q.append((nx,ny))

def solve():
    n = int(input())
    graph = []
    max_height = 0

    # 행별로 저장
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
        # 최대 높이
        max_height = max(max_height, max(row))

    result = 0

    for h in range(max_height):
        visited = [[False]*n for _ in range(n)]
        # 물에 잠기지 않은 영역의 개수
        count = 0

        for i in range(n):
            for j in range(n):
                if graph[i][j] > h and not visited[i][j]:
                    bfs(i,j,h,visited,n,graph)
                    count += 1

        result = max(result, count)
    print(result)

solve()



