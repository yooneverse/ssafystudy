from collections import deque

# 격자 크기 입력
N = int(input())

# 바다 상태 입력
# 0은 빈 칸
# 1~6은 물고기 크기
# 9는 아기 상어 위치
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

# 이동 방향 설정
# 위, 왼쪽, 오른쪽, 아래 순서
# 이 순서는 나중에 같은 거리의 물고기 중
# 가장 위, 가장 왼쪽을 선택하기 위함
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 아기 상어의 초기 위치 찾기
# 입력에서 9로 표시된 칸을 찾는다
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            sx, sy = i, j      # 상어 시작 좌표 저장
            board[i][j] = 0    # 시작 위치는 빈 칸으로 바꾼다

# 아기 상어의 초기 크기
size = 2

# 현재 크기에서 먹은 물고기 수
eat_cnt = 0

# 총 이동 시간
time = 0

# BFS 함수
# 현재 상어 위치에서 먹을 수 있는 모든 물고기를 찾는다
def bfs(x, y, size):
    # 방문 여부 체크 배열
    visited = [[False] * N for _ in range(N)]

    # BFS를 위한 큐
    # 좌표와 현재 거리(이동 시간)를 함께 저장
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True

    # 먹을 수 있는 물고기 후보들을 저장할 리스트
    # (거리, 행, 열) 형태로 저장한다
    fishes = []

    # BFS 시작
    while q:
        cx, cy, dist = q.popleft()

        # 네 방향으로 이동
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            # 격자 안에 있고 아직 방문하지 않은 칸인지 확인
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:

                # 상어가 지나갈 수 있는 조건
                # 빈 칸이거나
                # 상어 크기보다 작거나 같은 물고기
                if board[nx][ny] <= size:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))

                    # 실제로 먹을 수 있는 물고기 조건
                    # 물고기 크기가 상어 크기보다 작아야 한다
                    if 0 < board[nx][ny] < size:
                        fishes.append((dist + 1, nx, ny))

    # 먹을 수 있는 물고기 후보 리스트 반환
    return fishes

# 메인 시뮬레이션 반복
# 더 이상 먹을 수 있는 물고기가 없을 때까지 반복
while True:
    # 현재 위치에서 먹을 수 있는 물고기 탐색
    fishes = bfs(sx, sy, size)

    # 먹을 수 있는 물고기가 하나도 없으면 종료
    if not fishes:
        break

    # 거리, 행, 열 순으로 정렬
    # 문제 조건에 맞는 우선순위 선택을 위함
    fishes.sort()
    dist, fx, fy = fishes[0]

    # 물고기까지 이동한 시간만큼 누적
    time += dist

    # 물고기 한 마리 섭취
    eat_cnt += 1

    # 먹은 자리 비우기
    board[fx][fy] = 0

    # 상어 위치 갱신
    sx, sy = fx, fy

    # 현재 크기만큼 물고기를 먹었다면 성장
    if eat_cnt == size:
        size += 1
        eat_cnt = 0

# 총 걸린 시간 출력
print(time)
