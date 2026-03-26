import sys

input = sys.stdin.readline

n, m = map(int, input().split())
sr, sc, sd = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))


def four(row, col):
    for dr, dc in delta:
        nr, nc = row + dr, col + dc
        if 0 <= nr < n and 0 <= nc < m and not grid[nr][nc] and not visited[nr][nc]:
            return False
    return True


def cleaner(row, col, direction):
    answer = 0
    r, c, d = row, col, direction
    while True:
        if not grid[r][c] and not visited[r][c]:
            visited[r][c] = 1
            answer += 1
            grid[r][c] = 0
        elif four(r, c):
            tmp = (d + 2) % 4
            tr, tc = r + delta[tmp][0], c + delta[tmp][1]
            if 0 <= tr < n and 0 <= tc < m and not grid[tr][tc]:
                r, c = tr, tc
            else:
                break
        else:
            d = (d + 3) % 4
            tr, tc = r + delta[d][0], c + delta[d][1]
            if 0 <= tr < n and 0 <= tc < m and not grid[tr][tc] and not visited[tr][tc]:
                r, c = tr, tc
    return answer


answer = cleaner(sr, sc, sd)

print(answer)
