import sys
input = sys.stdin.readline

from heapq import heappop, heappush

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

def check(r, c):
    return 0 <= r < N and 0 <= c < M

def dijkstra():
    dists = [[10001] * M for _ in range(N)]
    dists[0][0] = 0

    start = [(0, 0, 0)]

    while start:
        dist, r, c = heappop(start)

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if not check(nr, nc):
                continue
            nxt_dist = dist + grid[nr][nc]
            if dists[nr][nc] <= nxt_dist:
                continue

            if nr == N - 1 and nc == M - 1:
                return nxt_dist

            heappush(start, (nxt_dist, nr, nc))
            dists[nr][nc] = nxt_dist
    return 0

M, N = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

print(dijkstra())
