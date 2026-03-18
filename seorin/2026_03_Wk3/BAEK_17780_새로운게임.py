''' 
N*N 말 K개 
체스판 = 흰 / 파 / 빨 
이동 방향 = 위 / 아래 / 왼쪽 / 오른쪽
말끼리 겹칠 수 있고 말이 이동할 떄 위에 올려진 말도 함께 이동 (가장 아래 있는 말만 이도 가능)
말이 4개 되면 게임 종료

A말 기준
1. 흰색 -> 그 칸으로 이동
- 움직이는 칸에 다른 게 있으면 A를 가장 위로 올림
- A 위에 다른 말이 있으면 같이 이동

2. 빨간색 
- 말 없는 경우 : 순서 다 바꾸기 (역순 -> 슬라이싱 하면 될 듯)
- 기존 말 있는 경우 : 기존 말은 놔두고 그 위에 역순으로 올리기 

3. 파란색 
- 말의 이동 방향을 반대로 하고 한 칸 이동 
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]


pieces = [None] * K
# 각 칸에 쌓인 말 번호 리스트
stack = [[[] for _ in range(N)] for _ in range(N)]

for i in range(K):
    r, c, d = map(int, input().split())
    pieces[i] = [r - 1, c - 1, d - 1]  
    stack[r - 1][c - 1].append(i)

def reverse_dir(d):
    if d == 0: return 1
    if d == 1: return 0
    if d == 2: return 3
    return 2

def move(piece_num):
    r, c, d = pieces[piece_num]
    nr, nc = r + di[d], c + dj[d]

    # 파란색이거나 범위 밖 -> 방향 반대로
    if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] == 2:
        d = reverse_dir(d)
        pieces[piece_num][2] = d
        nr, nc = r + di[d], c + dj[d]

        # 다시 파란색이거나 범위 밖 -> 이동 안함
        if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] == 2:
            return False

    # 현재 칸에서 이동할 말들 추출 
    idx = stack[r][c].index(piece_num)
    moving = stack[r][c][idx:]
    stack[r][c] = stack[r][c][:idx]

    # 흰색 -> 그대로 올리기
    if board[nr][nc] == 0:
        for p in moving:
            pieces[p][0], pieces[p][1] = nr, nc
        stack[nr][nc].extend(moving)

    # 빨간색 -> 역순으로 올리기
    elif board[nr][nc] == 1:
        moving.reverse()
        for p in moving:
            pieces[p][0], pieces[p][1] = nr, nc
        stack[nr][nc].extend(moving)

    # 4개 이상 쌓이면 종료
    return len(stack[nr][nc]) >= 4

turn = 0
while turn <= 1000:
    turn += 1
    over = False

    for i in range(K):
        r, c, _ = pieces[i]
        # 가장 아래 말만 이동 가능
        if stack[r][c][0] != i:
            continue

        if move(i):
            over = True
            break

    if over:
        break

print(turn if turn <= 1000 else -1)
