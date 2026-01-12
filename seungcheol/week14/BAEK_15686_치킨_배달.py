import sys
input = sys.stdin.readline

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

def dfs(idx):
    global answer
    if len(survive) == M:
        dist = 0
        for r, c in house:
            tmp = INF
            for i, j in survive:
                tmp = min(tmp, abs(r - i) + abs(c - j))
            dist += tmp
        answer = min(answer, dist)
        return
    else:
        for i in range(idx + 1, cnt_chicken):
            survive.append(chicken[i])
            dfs(i)
            survive.pop()

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
survive = []

for row in range(N):
    for col in range(N):
        if grid[row][col] == 1:
            house.append((row, col))
        elif grid[row][col] == 2:
            chicken.append((row, col))

cnt_house = len(house)
cnt_chicken = len(chicken)

INF = float("inf")
answer = INF

dfs(-1)

print(answer)

# # 최초 풀이
# from collections import deque
# from itertools import combinations
#
# delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
#
# def check(r, c):
#     return 0 <= r < N and 0 <= c < N
#
# def bfs(sr, sc, cnt):
#     visited = [0] * N
#
#     q = deque([(sr, sc, 0)])
#     while q:
#         sr, sc, dist = q.popleft()
#         for dr, dc in delta:
#             nr = sr + dr
#             nc = sc + dc
#             if not check(nr, nc):
#                 continue
#             if visited[nr] & (1 << nc):
#                 continue
#             if grid[nr][nc] == 2:
#                 distance[cnt][chicken[(nr, nc)]] = dist + 1
#             q.append((nr, nc, dist + 1))
#             visited[nr] |= (1 << nc)
#     return
#
# N, M = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(N)]
#
# house = []
# chicken = {}
# cnt_chicken = 0
#
# for row in range(N):
#     for col in range(N):
#         if grid[row][col] == 1:
#             house.append((row, col))
#         elif grid[row][col] == 2:
#             chicken[(row, col)] = cnt_chicken
#             cnt_chicken += 1
#
# cnt_house = len(house)
# distance = [[0] * cnt_chicken for _ in range(cnt_house)]
#
# cnt = 0
# for r, c in house:
#     bfs(r, c, cnt)
#     cnt += 1
# INF = float("inf")
# answer = INF
# comb = [i for i in range(cnt_chicken)]
# for co in combinations(comb, M):
#     tmp = 0
#     for d in distance:
#         min_d = INF
#         for c in co:
#             min_d = min(min_d, d[c])
#         tmp += min_d
#     answer = min(answer, tmp)
#
# print(answer)