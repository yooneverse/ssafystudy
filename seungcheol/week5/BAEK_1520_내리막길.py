from collections import deque

M, N = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(M)]

que = deque([(0, 0)])

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

result = 0

while que:
    start = que.popleft()

    if start == (M - 1, N - 1):
        result += 1
    for di, dj in delta:
        ni = start[0] + di
        nj = start[1] + dj
        if 0 <= ni < M and 0 <= nj < N and matrix[start[0]][start[1]] > matrix[ni][nj]:
            que.append((ni, nj))

print(result)