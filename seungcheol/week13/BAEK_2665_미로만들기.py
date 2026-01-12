from heapq import heappush, heappop

def check(r, c):
    return 0 <= r < N and 0 <= c < N

def bfs(goal):
    pq = []
    heappush(pq, (0, 0, 0))
    visited[0][0] = 1

    while pq:
        cnt, row, col = heappop(pq)
        if row == col == goal:
            return cnt
        for dr, dc in delta:
            nr = row + dr
            nc = col + dc
            if not check(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = 1
            if grid[nr][nc]:
                heappush(pq, (cnt, nr, nc))
            else:
                heappush(pq, (cnt + 1, nr, nc))
    return 0


N = int(input())
grid = [list(map(int, input())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

delta = ((-1, 0), (0, -1), (1, 0), (0, 1))

print(bfs(N - 1))
