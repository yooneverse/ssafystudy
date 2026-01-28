# https://www.acmicpc.net/problem/17144
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치(두 행, 0열)
upper = lower = -1
for y in range(R):
    if board[y][0] == -1:
        if upper == -1:
            upper = y
        else:
            lower = y
            break

# 확산: tmp에 누적 후 한 번에 반영
def diffuse():
    tmp = [[0]*C for _ in range(R)]
    tmp[upper][0] = -1
    tmp[lower][0] = -1

    for r in range(R):
        br = board[r]
        for c in range(C):
            val = br[c]
            if val <= 0:   # 0 또는 -1
                continue
            spread = val // 5
            if spread == 0:
                tmp[r][c] += val
                continue

            remain = val
            nr = r - 1
            if nr >= 0 and board[nr][c] != -1:
                tmp[nr][c] += spread
                remain -= spread
            nr = r + 1
            if nr < R and board[nr][c] != -1:
                tmp[nr][c] += spread
                remain -= spread
            nc = c - 1
            if nc >= 0 and board[r][nc] != -1:
                tmp[r][nc] += spread
                remain -= spread
            nc = c + 1
            if nc < C and board[r][nc] != -1:
                tmp[r][nc] += spread
                remain -= spread

            tmp[r][c] += remain
    return tmp

# 상부(반시계)
def wind_upper():
    y = upper
    # 왼쪽 열: 위로
    for r in range(y-1, 0, -1):
        board[r][0] = board[r-1][0]
    # 윗 행: 왼쪽으로
    for c in range(0, C-1):
        board[0][c] = board[0][c+1]
    # 오른쪽 열: 아래로
    for r in range(0, y):
        board[r][C-1] = board[r+1][C-1]
    # 청정기 행: 오른쪽으로
    for c in range(C-1, 1, -1):
        board[y][c] = board[y][c-1]
    board[y][1] = 0
    board[y][0] = -1

# 하부(시계)
def wind_lower():
    y = lower
    # 왼쪽 열: 아래로
    for r in range(y+1, R-1):
        board[r][0] = board[r+1][0]
    # 아랫 행: 왼쪽으로
    for c in range(0, C-1):
        board[R-1][c] = board[R-1][c+1]
    # 오른쪽 열: 위로
    for r in range(R-1, y, -1):
        board[r][C-1] = board[r-1][C-1]
    # 청정기 행: 오른쪽으로
    for c in range(C-1, 1, -1):
        board[y][c] = board[y][c-1]
    board[y][1] = 0
    board[y][0] = -1

for _ in range(T):
    board = diffuse()
    wind_upper()
    wind_lower()

# 합산(청정기 제외)
ans = 0
for r in range(R):
    for c in range(C):
        if board[r][c] > 0:
            ans += board[r][c]
print(ans)
