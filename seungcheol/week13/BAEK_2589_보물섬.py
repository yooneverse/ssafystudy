# from collections import deque
#
# import sys
# input = sys.stdin.readline
#
# def check(r, c):
#     return 0 <= r < R and 0 <= c < C
#
# def bfs(sr, sc):
#     q = deque([(sr, sc, 0)])
#     while q:
#         r, c, d = q.popleft()
#         for dr, dc in delta:
#             nr = r + dr
#             nc = c + dc
#             if not check(nr, nc):
#                 continue
#             if visited[nr] & (1 << nc):
#                 continue
#             if grid[nr][nc] == 'W':
#                 continue
#             q.append((nr, nc, d + 1))
#             visited[nr] = visited[nr] | (1 << nc)
#
#     r, c = find_answer(r, c)
#     find_answer(r, c)
#
#
# def find_answer(sr, sc):
#     global answer
#     visited2 = [0] * R
#     q = deque([(sr, sc, 0)])
#     visited2[sr] = visited2[sr] | (1 << sc)
#
#     while q:
#         r, c, d = q.popleft()
#         for dr, dc in delta:
#             nr = r + dr
#             nc = c + dc
#             if not check(nr, nc):
#                 continue
#             if visited2[nr] & (1 << nc):
#                 continue
#             if grid[nr][nc] == 'W':
#                 continue
#             q.append((nr, nc, d + 1))
#             visited2[nr] = visited2[nr] | (1 << nc)
#     answer = max(answer, d)
#
#     return r, c
#
#
# delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
#
# R, C = map(int, input().split())
# grid = list(input().strip() for _ in range(R))
# visited = [0] * R
#
# answer = 0
#
# for i in range(R):
#     for j in range(C):
#         if grid[i][j] == 'W':
#             continue
#         if visited[i] & (1 << j):
#             continue
#         visited[i] = visited[i] | (1 << j)
#         bfs(i, j)
#
# print(answer)
#

from collections import deque

import sys
input = sys.stdin.readline

def check(r, c):
    return 0 <= r < R and 0 <= c < C

def bfs(sr, sc):
    global answer
    visited = [0] * R
    visited[sr] = visited[sr] | (1 << sc)
    q = deque([(sr, sc, 0)])
    while q:
        r, c, d = q.popleft()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if not check(nr, nc):
                continue
            if visited[nr] & (1 << nc):
                continue
            if grid[nr][nc] == 'W':
                continue
            q.append((nr, nc, d + 1))
            visited[nr] = visited[nr] | (1 << nc)
    answer = max(answer, d)



delta = ((-1, 0), (0, -1), (1, 0), (0, 1))

R, C = map(int, input().split())
grid = list(input().strip() for _ in range(R))

answer = 0

for i in range(R):
    for j in range(C):
        if grid[i][j] == 'W':
            continue
        if 0 < i < R - 1 and 0 < j < C - 1 and (grid[i - 1][j], grid[i][j - 1], grid[i + 1][j], grid[i][j + 1]) == ('L', 'L', 'L', 'L'):
            continue
        bfs(i, j)

print(answer)
