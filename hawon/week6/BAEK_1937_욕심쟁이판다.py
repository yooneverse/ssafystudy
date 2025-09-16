# 델타 상하좌우 배열
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def panda_moving(sr, sc):
    # 만약 방문했던 곳이면 또 방문하지 않고 값 리턴
    if dp[sr][sc] != 0:
        return dp[sr][sc]

    # 자기 자신 포함하기
    dp[sr][sc] = 1

    # 델타로 이동하기
    for k in range(4):
        nr = sr + dr[k]
        nc = sc + dc[k]
        # 만약 범위 안에 있고 현재 좌표보다 대나무가 많으면
        if 0<=nr<N and 0<=nc<N and matrix[nr][nc] > matrix[sr][sc]:
            # 판다는 먹으러 간다
            # 다음 범위로 움직일 수 있다면, 현재 좌표에 움직일 수 있다고 숫자를 더해서 올려줘야 함
            dp[sr][sc] = max(dp[sr][sc], 1 + panda_moving(nr, nc))
    
    # 돌려줘 이동 길이
    return dp[sr][sc]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 원하는 답
max_val = 0

# dp[r][c]는 최대로 갈 수 있는 수
dp = [[0] * N for _ in range(N)]

# 시작점 정해주는 동시에 함수 호출
for r in range(N):
    for c in range(N):
        max_val = max(panda_moving(r,c), max_val)

print(max_val)


############### 시간초과 ##################
# 델타 상하좌우 배열
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def panda_moving(sr, sc, move):
    global max_val
    # 가지치기
    # 현재까지 길이를 최댓값과 비교
    max_val = max(move, max_val)

    # 델타로 이동하기
    for k in range(4):
        nr = sr + dr[k]
        nc = sc + dc[k]
        # 만약 범위 안에 있고 현재 좌표보다 대나무가 많으면
        if 0<=nr<N and 0<=nc<N and matrix[nr][nc] > matrix[sr][sc]:
            # 판다는 먹으러 간다
            panda_moving(nr, nc, move+1)


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 원하는 답
max_val = 0

# 시작점 정해주는 동시에 함수 호출
for r in range(N):
    for c in range(N):
        panda_moving(r, c, 1)

print(max_val)