# bfs
from collections import deque

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():
    # r, c, 포탄 수, 이동 거리
    q = deque([(0, 0, 1, 1)])
    visited[0][0][1] = 1

    while q:
        r, c, bullet, dist = q.popleft()

        if (r, c) == (N - 1, M - 1):
            return dist

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if maze[nr][nc] == 1 and bullet == 1:
                if visited[nr][nc][0]:
                    continue
                visited[nr][nc][0] = 1
                q.append((nr, nc, 0, dist + 1))
            elif maze[nr][nc] == 0:
                if visited[nr][nc][bullet]:
                    continue
                visited[nr][nc][bullet] = 1
                q.append((nr, nc, bullet, dist + 1))
    return -1

N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

answer = bfs()

print(answer)
