import sys
import heapq

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * M for _ in range(N)]
    dp[0][0] = 1

    pq = [(-board[0][0], 0, 0)]

    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while pq:
        h, x, y = heapq.heappop(pq)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] < board[x][y]:
                    dp[nx][ny] += dp[x][y]
                    
                    if not visited[nx][ny]:
                        heapq.heappush(pq, (-board[nx][ny], nx, ny))
                        visited[nx][ny] = True

    print(dp[N-1][M-1])

solve()