import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
sr, sc, gr, gc = map(int, input().split())

grid = [list(input().strip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

def bfs(lst):
    que = deque(lst)
    nxt = []
    while que:
        r, c = que.popleft()

        for dr, dc in delta:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                visited[nr][nc] = 1
                if grid[nr][nc] == '0':
                    que.append((nr, nc))
                elif grid[nr][nc] == '1':
                    nxt.append((nr, nc))
                elif grid[nr][nc] == '#':
                    return 0
    return nxt

answer = 0
jump = [(sr - 1, sc - 1)]
visited[sr - 1][sc - 1] = 1
while jump:
    answer += 1
    jump = bfs(jump)

print(answer)
