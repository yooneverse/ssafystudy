import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = []
max_h = 0
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    # 가장 높은 높이 저장
    for v in row:
        if v > max_h:
            max_h = v

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

best = 1  # 비가 아예 안 오면(0) 최소 1개는 나올 수 있으니 기본 1

# 비의 높이 h를 0부터 max_h-1까지 검사
for h in range(0, max_h):
    visited = []
    for _ in range(N):
        visited.append([False] * N)

    safe_cnt = 0

    # 아직 방문 안 했고 물에 안 잠긴 칸이면 ㄱ
    for r in range(N):
        for c in range(N):
            if visited[r][c] == False and arr[r][c] > h:
                safe_cnt += 1

                q = deque()
                q.append((r, c))
                visited[r][c] = True

                while q:
                    cr, cc = q.popleft()

                    for k in range(4):
                        nr = cr + dr[k]
                        nc = cc + dc[k]

                        if 0 <= nr < N and 0 <= nc < N:
                            if visited[nr][nc] == False and arr[nr][nc] > h:
                                visited[nr][nc] = True
                                q.append((nr, nc))

    if safe_cnt > best:
        best = safe_cnt

print(best)
