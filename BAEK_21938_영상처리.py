from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 평균 밝기값만 저장할 2차원 배열
screen = []

for _ in range(N):
    row = list(map(int, input().split()))

    # 이 줄의 각 픽셀 밝기 평균을 저장할 리스트
    temp = []

    # j번째 픽셀의 R, G, B 값 꺼내기
    for j in range(M):
        r = row[3 * j]
        g = row[3 * j + 1]
        b = row[3 * j + 2]
        avg = (r + g + b) // 3
        temp.append(avg)

    screen.append(temp)

T = int(input())

# 기준값 T로 이진화
for i in range(N):
    for j in range(M):
        if screen[i][j] >= T:
            screen[i][j] = 255
        else:
            screen[i][j] = 0

visited = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and screen[nx][ny] == 255:
                    visited[nx][ny] = True
                    q.append((nx, ny))

# 객체(연결 요소) 개수
count = 0

for i in range(N):
    for j in range(M):
        if screen[i][j] == 255 and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)