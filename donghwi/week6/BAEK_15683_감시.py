# chatgpt 비율 70%임을 밝힙니다.

dr = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dc = [0, 1, 0, -1]

# CCTV별 가능한 방향 묶음
cctv_dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}


def dfs(idx):
    global result
    if idx == len(cctvs):
        # 사각지대(0) 개수 세기
        blind = 0
        for row in board:
            blind += row.count('0')
        result = min(result, blind)
        return

    y, x, t = cctvs[idx]

    for dirs in cctv_dir[t]:
        changed = []  # 이번 배치에서 새로 감시로 바꾼 좌표들 기록

        # 각 방향으로 쏘면서 표시
        for d in dirs:
            ny, nx = y, x
            while True:
                ny += dr[d]
                nx += dc[d]
                if not (0 <= ny < N and 0 <= nx < M):
                    break
                if board[ny][nx] == '6':
                    break  # 벽이면 중단
                if board[ny][nx] == '0':
                    board[ny][nx] = '#'  # 감시됨 표시
                    changed.append((ny, nx))
                # 다른 CCTV나 이미 감시('#')인 칸은 그냥 통과

        dfs(idx + 1)

        # 롤백
        for cy, cx in changed:
            board[cy][cx] = '0'


N, M = map(int, input().split())
board = [list(input().split()) for _ in range(N)]

# CCTV 목록 수집 (문자 유지, 필요시 int 변환)
cctvs = []
for i in range(N):
    for j in range(M):
        if board[i][j] in '12345':
            cctvs.append((i, j, int(board[i][j])))

result = N * M  # 충분히 큰 값으로 시작

dfs(0)
print(result)
