import sys
from collections import deque

input = sys.stdin.readline

# M: 세로(행), N: 가로(열), K: 직사각형 개수
M, N, K = map(int, input().split())

# board[y][x] = 1이면 직사각형으로 막힌 칸, 0이면 빈 칸
board = [[0] * N for _ in range(M)]

# 직사각형 칠하기: (x1, y1) ~ (x2, y2), x2/y2는 포함하지 않음
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = 1

# 4방향 이동 (상, 하, 좌, 우)
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

areas = []

for y in range(M):
    for x in range(N):
        # 빈 칸(0)이면서 아직 방문 안 했으면(=0) BFS 시작
        if board[y][x] == 0:
            q = deque()
            q.append((y, x))
            board[y][x] = 1  # 방문 처리(다시 안 오게 막아버림)

            area = 1  # 현재 영역 넓이

            while q:
                cy, cx = q.popleft()

                for d in range(4):
                    ny = cy + dy[d]
                    nx = cx + dx[d]

                    # 범위 체크
                    if 0 <= ny < M and 0 <= nx < N:
                        # 빈 칸이면 방문 처리 후 확장
                        if board[ny][nx] == 0:
                            board[ny][nx] = 1
                            q.append((ny, nx))
                            area += 1

            areas.append(area)

areas.sort()

print(len(areas))
print(*areas)