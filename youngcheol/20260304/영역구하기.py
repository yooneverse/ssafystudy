
M, N, K = map(int, input().split())

grid = [[0] * N for _ in range(M)]

# 직사각형 좌표 입력받고 칠하기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            grid[y][x] = 1

# 상, 하, 좌, 우 
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

#각 영역의 넓이를 담을 스택
matrix = []
cnt = 0

for i in range(M):
    for j in range(N):
        if grid[i][j] == 0:
            cnt += 1

            stack = [(i, j)]
            grid[i][j] = 1 # 기존 방문한곳은 1로 처리
            area = 0
            
            # 여기서 너무 헤맸습니다 오랜만에 하는거라 기억이 잘 안나더라고요 
            while stack:
                cy, cx = stack.pop()
                area += 1
                
                for d in range(4):
                    ny = cy + dy[d]
                    nx = cx + dx[d]
                    
                    # 영역이 있을 수 있는 범위 
                    if 0 <= ny < M and 0 <= nx < N and grid[ny][nx] == 0:
                        grid[ny][nx] = 1
                        stack.append((ny, nx))
                        
            matrix.append(area)
# 넓이 오른차순 정리
matrix.sort()

print(cnt)
print(*matrix)