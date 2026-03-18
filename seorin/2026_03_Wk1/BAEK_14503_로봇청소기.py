'''
현재 위치 청소
반시계 방향으로 회전하며 청소 안 된 칸 탐색
이동하면 다시 청소 시작

4칸 모두 청소되어 있거나 벽이면
뒤로 한 칸 후진

뒤가 벽이면 작동 종료
'''

n, m = map(int, input().split()) # 방 크기 
r, c, d = map(int, input().split()) # 좌표, 방향
board = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]  
dy = [0, 1, 0, -1]


def clean(x, y, d):
    cnt = 0

    while True:

        # 현재 칸 청소
        if board[x][y] == 0:
            board[x][y] = -1
            cnt += 1

        moved = False

        # 반시계 방향 회전하면서 탐색
        for _ in range(4):
            d = (d - 1) % 4
            nx, ny = x + dx[d], y + dy[d]

            # 청소 안 된 칸이면 이동
            if board[nx][ny] == 0:
                x, y = nx, ny
                moved = True
                break

        # 이동했으면 다시 청소 시작
        if moved:
            continue

        # 네 방향 모두 청소 or 벽이면 후진
        bx, by = x - dx[d], y - dy[d]

        # 뒤가 벽이면 종료
        if board[bx][by] == 1:
            print(cnt)
            return

        x, y = bx, by


clean(r, c, d)