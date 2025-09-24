from collections import deque

n, m = map(int, input().split())

# 0(색칠 안 됨), 1(색칠 됨)
board = [list(map(int, input().split())) for _ in range(n)]


visited = [[0] * m for _ in range(n)]

# 4방향 이동 벡터 (상, 하, 좌, 우)
DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 1  # 시작 
    area = 1                # 시작 칸(1) 포함 넓이 1부터 시작

    while q:
        r, c = q.popleft()

        # 4방향으로 인접한 칸 확인
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc

            # 1) 범위 안인지 확인
            if not (0 <= nr < n and 0 <= nc < m):
                continue

            # 2) 아직 방문하지 않았고 색칠된 곳이라면
            if not visited[nr][nc] and board[nr][nc] == 1:
                visited[nr][nc] = 1  # 방문 처리
                q.append((nr, nc))      # 큐에 추가
                area += 1               # 넓이(1의 개수) 증가

    return area  # 시작점과 연결된 모든 1을 탐색한 결과 넓이 반환

count = 0     # 그림의 개수
max_area = 0  # 가장 넓은 그림의 넓이

# 아직 방문하지 않은 '1'을 시작점으로 BFS를 실행
for i in range(n):
    for j in range(m):
        # 색칠되어 있고 아직 방문하지 않은 칸이면 새로운 그림의 시작
        if board[i][j] == 1 and not visited[i][j]:
            count += 1                  # 그림 개수 1 증가
            max_area = max(max_area, bfs(i, j))  # 해당 그림 넓이로 최댓값 갱신

print(count)
print(max_area)