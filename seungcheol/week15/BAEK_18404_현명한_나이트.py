import sys
input = sys.stdin.readline

from collections import deque

def check(r, c):
    return 0 <= r < N and 0 <= c < N
def bfs(sr, sc):
    visited[sr][sc] = 0
    q = deque([(sr, sc, 0)])
    while q:
        r, c, dist = q.popleft()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if not check(nr, nc):
                continue
            if visited[nr][nc] != -1:
                continue
            visited[nr][nc] = dist + 1
            q.append((nr, nc, dist + 1))


delta = ((-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, 1), (1, 2), (2, -1), (1, -2))

N, M = map(int, input().split())
R, C = map(int, input().split())

visited = [[-1] * N for _ in range(N)]

bfs(R - 1, C - 1)

for _ in range(M):
    x, y = map(int, input().split())
    print(visited[x - 1][y - 1], end=' ')
