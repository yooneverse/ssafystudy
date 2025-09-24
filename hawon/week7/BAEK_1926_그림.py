from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r,c):
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    cnt = 1
    while q:
        qr, qc = q.popleft()

        for k in range(4):
            nr = qr + dr[k]
            nc = qc + dc[k]
            if 0<=nr<N and 0<=nc<M and grid[nr][nc] != 0:
                if visited[nr][nc] == 0:
                    q.append((nr,nc))
                    visited[nr][nc] = 1
                    cnt += 1
    return cnt

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 알고 싶은 값 : 그림 개수, 제일 넓은 그림
result = 0
cnt = 0

visited = [[0] * M for _ in range(N)]

for r in range(N):
    for c in range(M):
        if grid[r][c] == 1 and visited[r][c] == 0:
            picture = bfs(r,c)
            result = max(result, picture)
            cnt +=1

print(cnt)
print(result)