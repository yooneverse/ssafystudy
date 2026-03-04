'''
BAEK_2583_영역 구하기
직사각형으로 칠해진 칸을 막아두기
안 칠해진 칸들이 서로 붙어서 만들어지는 “빈 영역”이 몇 개인지 + 각 영역 넓이가 몇 칸인지
'''
from collections import deque


N, M, K = map(int, input().split())

grid = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            grid[y][x] = 1

visited = [[0] * N for _ in range(M)]

# 4방향
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

areas = []

for i in range(M):        
    for j in range(N): 
        # 빈칸이고 아직 방문 안 했으면 -> 새 영역 시작
        if grid[i][j] == 0 and visited[i][j] == 0:
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            cnt = 1
            
            while q:
                y, x = q.popleft()

                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]

                    # 격자 밖이면 패스
                    if ny < 0 or ny >= M or nx < 0 or nx >= N:
                        continue

                    # 빈칸이고 방문 안 했으면 확장
                    if grid[ny][nx] == 0 and visited[ny][nx] == 0:
                        visited[ny][nx] = 1
                        q.append((ny, nx))
                        cnt += 1

            areas.append(cnt)

areas.sort()
print(len(areas))
print(*areas)