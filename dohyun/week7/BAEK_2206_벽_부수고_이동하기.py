# BAEK 2206. 벽 부수고 이동하기
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
grid = [str(input()) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 벽을 부순 경우와 아닌 경우를 나누기 위해 N * N * 2 배열 사용
visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
# y, x 좌표와 벽을 부술 수 있는 횟수 덱에 저장
q = deque([(0, 0, 1)])
visited[0][0][1] = 1

# 덱 진행
while q:
    y, x, cnt = q.popleft()

    # 상하좌우 배열 범위 확인
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if not (0 <= ny < N and 0 <= nx < M):
            continue

        # 벽이 없고 방문한 적이 없을 때
        if grid[ny][nx] == '0' and visited[ny][nx][cnt] == -1:
            visited[ny][nx][cnt] = visited[y][x][cnt] + 1
            q.append((ny, nx, cnt))

        # 벽이 있고 부술 수 있으며 방문한 적이 없을 때
        elif grid[ny][nx] == '1' and cnt == 1 and visited[ny][nx][0] == -1:
            visited[ny][nx][0] = visited[y][x][cnt] + 1
            q.append((ny, nx, 0))

# 통과 못 했을 때 대비해서 결과값 설정
ans = -1
# 벽을 부쉈을 때 방문한 칸 수
v0 = visited[N-1][M-1][0]\
    # 벽을 부수지 않았을 때 방문한 칸 수
v1 = visited[N-1][M-1][1]

# 둘 중 더 작은 수를 결과값으로 저장
if v0 != -1 and v1 != -1:
    if v0 < v1:
        res = v0
    else:
        res = v1
# 한 쪽 값이 없을 때는 바로 저장
elif v0 != -1:
    res = v0
elif v1 != -1:
    res = v1

print(res)
