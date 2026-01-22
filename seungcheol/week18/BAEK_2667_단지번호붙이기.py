import sys
input = sys.stdin.readline

from collections import deque

delta = ((0, 1), (0, -1), (1, 0), (-1, 0))

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = 1
    dist = 0
    while q:
        sr, sc = q.popleft()
        dist += 1
        for dr, dc in delta:
            nr = sr + dr
            nc = sc + dc
            if not in_range(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            if house[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
    return dist

N = int(input().strip())
house = [list(map(int, input().strip())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
answer = []

for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        if house[i][j]:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for num in answer:
    print(num)
