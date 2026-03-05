N, M = map(int, input().split())
r, c, d = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

clean = 0

while True:
    # 1) 현재 칸 청소
    if box[r][c] == 0:
        box[r][c] = -1
        clean += 1

    # 2) 주변 4칸 탐색
    moved = False
    for _ in range(4):
        d = (d + 3) % 4     # 왼쪽으로 회전
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            r, c = nx, ny
            moved = True
            break

    if moved:
        continue

    # 3) 네 방향 모두 불가 → 뒤로 이동
    back = (d + 2) % 4
    br = r + dx[back]
    bc = c + dy[back]

    if not (0 <= br < N and 0 <= bc < M) or box[br][bc] == 1:
        break  # 뒤쪽이 벽이면 종료

    r, c = br, bc

print(clean)
