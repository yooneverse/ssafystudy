from collections import deque

night = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 0

    while q:
        qr, qc = q.popleft()
        for move_r, move_c in night:
            nr = qr + move_r
            nc = qc + move_c
            if 0<=nr<N and 0<=nc<N:
                if visited[nr][nc] == -1:
                    visited[nr][nc] = visited[qr][qc] + 1
                    q.append((nr,nc))


N, M = map(int, input().split())

# 좌표가 0부터 시작하므로 -1 해주기
x, y = map(int, input().split())
x -=1
y -=1

arr = []
for _ in range(M):
    a, b = map(int, input().split())
    a -=1
    b -=1
    arr.append([a,b])

visited = [[-1] * N for _ in range(N)]
bfs(x,y)

res = []
for vr, vc in arr:
    res.append(visited[vr][vc])

print(*res)