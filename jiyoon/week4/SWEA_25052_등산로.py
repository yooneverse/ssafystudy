# 어떻게든 DFS에 구겨 넣기

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, length):
    global max_way
    if length > max_way:
        max_way = length

    # 현재 칸보다 낮은 이웃 중 가장 낮은 값 찾기
    min_val = matrix[x][y]
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] < min_val:
                min_val = matrix[nx][ny]

    # 더 낮은 칸이 없으면 종료
    if min_val == matrix[x][y]:
        return

    # 가장 낮은 칸이 여러 개일 수 있으므로 DFS 분기
    for d in range(4):
        nx= x + dx[d] 
        ny= y + dy[d]
        if 0 <= nx < N and 0 <= ny < N: # 구간 내에 있는지 확인
            if matrix[nx][ny] == min_val: #좌표 값이 최소 값이라면
                dfs(nx, ny, length + 1)

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_way = 0
    for i in range(N):
        for j in range(N):
            dfs(i, j, 1)   # 모든 칸에서 출발 가능함

    print(f"#{tc} {max_way}")

