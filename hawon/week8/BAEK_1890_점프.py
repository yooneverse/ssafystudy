# Todo : 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로
# start = (0,0) / end = (N-1,N-1)
# 반드시 오른쪽이나 아래쪽으로만 이동해야 한다. (칸에 적혀있는 수만큼)
# 0은 이동 X
# 점프할 때 방향 바꾸기 x

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1  # 시작점 1

for r in range(N):
    for c in range(N):
        # 점프할 거리
        jump = board[r][c]
        if jump == 0: 
            continue  # 0이면 못 뜀
            
        # 아래로
        # 보드 안이면 현재까지의 경우의 수를 아래칸에 더한다
        nr = r + jump
        if nr < N:
            dp[nr][c] += dp[r][c]
        # 오른쪽으로
        # 보드 안이면 현재까지의 경우의 수를 오른쪽칸에 더한다
        nc = c + jump
        if nc < N:
            dp[r][nc] += dp[r][c]

# 끝칸에 "도달"하는 전체 경우의 수
print(dp[N-1][N-1])