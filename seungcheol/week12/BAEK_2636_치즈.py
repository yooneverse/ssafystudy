import sys
from collections import deque

input = sys.stdin.readline

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

def bfs(cnt, q):
    num = len(q)
    next = deque([])
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if visited[nr][nc]:
                continue
            if grid[nr][nc]:
                next.append((nr, nc))
            else:
                q.append((nr, nc))
            visited[nr][nc] = 1
    if next:
        return bfs(cnt + 1, next)
    else:
        return cnt, num
R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
visited[0][0] = 1

deq = deque([(0, 0)])

for answer in bfs(0, deq):
    print(answer)
