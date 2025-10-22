from heapq import heappush, heappop

def dijkstra(sr, sc):
    pq = [(grid[sr][sc], sr, sc)]

    INF = float("inf")
    dists = [[INF] * n for _ in range(n)]

    while pq:
        dist, r, c = heappop(pq)
        if dists[r][c] < dist:
            continue

        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            new_dist = dist + grid[nr][nc]

            if new_dist >= dists[nr][nc]:
                continue
            dists[nr][nc] = new_dist
            heappush(pq, (new_dist, nr, nc))

    return dists[n-1][n-1]

cnt = 0
while True:
    n = int(input())

    if not n:
        break

    cnt += 1
    grid = [list(map(int, input().split())) for _ in range(n)]

    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    answer = dijkstra(0, 0)

    print(f"Problem {cnt}: {answer}")

# # 인접 리스트
# def dijkstra(sr, sc):
#     pq = [(0, sr, sc)]
#
#     INF = float("inf")
#     dists = [[INF] * n for _ in range(n)]
#     dists[sr][sc] = 0
#
#     while pq:
#         dist, r, c = heappop(pq)
#         if dists[r][c] < dist:
#             continue
#
#         for nxt_dist, nxt_r, nxt_c in edges[r][c]:
#             new_dist = dist + nxt_dist
#
#             if dists[nxt_r][nxt_c] <= new_dist:
#                 continue
#
#             dists[nxt_r][nxt_c] = new_dist
#             heappush(pq, (new_dist, nxt_r, nxt_c))
#
#     return dists[n-1][n-1]
#
# cnt = 0
# while True:
#     n = int(input())
#
#     if not n:
#         break
#
#     cnt += 1
#     grid = [list(map(int, input().split())) for _ in range(n)]
#
#     edges = [[[] for _ in range(n)] for _ in range(n)]
#
#     delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
#     for i in range(n):
#         for j in range(n):
#             for di, dj in delta:
#                 ni, nj = i + di, j + dj
#                 if ni < 0 or ni >= n or nj < 0 or nj >= n:
#                     continue
#                 edges[i][j].append((grid[i][j], ni, nj))
#
#     answer = dijkstra(0, 0) + grid[n-1][n-1]
#
#     print(f"Problem {cnt}: {answer}")
