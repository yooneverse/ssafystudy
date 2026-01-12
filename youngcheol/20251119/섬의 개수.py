# 가로 세로 대각선으로 연결되어 있는 사각형은 걸어갈 수 있다.

# 상하좌우 대각선
# 방향 배열 (상, 하, 좌, 우 + 대각선 4개 = 총 8방향)
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(si, sj):
    q = [[si, sj]]
    matrix[si][sj] = 0
    while q:
        ci, cj = q.pop(0)
        for d in range(8):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < h and 0 <= nj < w and matrix[ni][nj] == 1:
                matrix[ni][nj] = 0
                q.append([ni, nj])


while True:
    line = input().split()
    if not line: break
    w, h = map(int, line)
    if w == 0 and h == 0: break

    # --- [여기 부분이 바뀌었습니다] ---
    # h줄 만큼 입력을 받아 한 번에 2차원 리스트 생성
    matrix = [list(map(int, input().split())) for _ in range(h)]
    # -----------------------------

    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                cnt += 1
                bfs(i, j)
