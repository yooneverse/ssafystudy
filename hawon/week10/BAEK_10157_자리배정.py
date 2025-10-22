# 공연장 크기: C, R
C, R = map(int, input().split())
K = int(input())

# 좌석이 꽉 찼을 때보다 K가 크면 불가능
if K > C * R:
    print(0)
    exit()

# 상, 우, 하, 좌
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

# 좌석
board = [[0] * C for _ in range(R)]

# 시작 위치
r, c = R - 1, 0
dir_idx = 0  # 현재 방향 인덱스
cnt = 1
board[r][c] = cnt

# K번째 찾을 때까지 반복
while cnt < K:
    nr = r + drs[dir_idx]
    nc = c + dcs[dir_idx]

    # 다음 칸이 유효하고 아직 방문 안했으면 이동
    if (0 <= nr < R) and (0 <= nc < C) and board[nr][nc] == 0:
        cnt += 1
        r, c = nr, nc
        board[r][c] = cnt
    else:
        # 시계방향 전환
        dir_idx = (dir_idx + 1) % 4

print(c + 1, R - r)