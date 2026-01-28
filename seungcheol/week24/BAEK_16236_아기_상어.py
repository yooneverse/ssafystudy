import sys
input = sys.stdin.readline

from collections import deque

def check(r, c):
    return 0 <= r < n and 0 <= c < n

# 아기상어가 먹을 고기가 있는지 확인
# 있으면 아기상어 이동, 경험치 증가, 경험치 가득 차면 크기 증가, 이동 거리만큼 시간 경과
# 없으면 종료
def bfs(start):
    global answer, exp, level

    row, col = start
    que = deque([(0, row, col)])
    visited = [[0] * n for _ in range(n)]
    visited[row][col] = 1

    # 다음 먹을 생선 위치
    fish = (n, n)

    # 다음 생선까지의 거리
    nxt_dist = 0

    while que:
        dist, r, c = que.popleft()

        # 가장 가까운 생선 확정
        if nxt_dist and nxt_dist == dist:
            break

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc

            if not check(nr, nc):
                continue

            if visited[nr][nc]:
                continue

            # 이동 위치의 생선이 크면 이동 불가
            if grid[nr][nc] > level:
                continue

            que.append((dist + 1, nr, nc))
            visited[nr][nc] = 1

            # 먹을 수 있는 생선
            if grid[nr][nc] and grid[nr][nc] < level:
                # 위에 있는가?
                if nr < fish[0]:
                    fish = (nr, nc)
                    nxt_dist = dist + 1
                # 같은 높이면 왼쪽인가?
                elif nr == fish[0] and nc < fish[1]:
                    fish = (nr, nc)
                    nxt_dist = dist + 1

    # 먹을 생선이 있다면
    if nxt_dist:
        grid[fish[0]][fish[1]] = 9
        grid[row][col] = 0
        answer += nxt_dist
        exp += 1
        if exp == level:
            level += 1
            exp = 0
        return True, fish

    # 먹을 생선이 없다면
    return False, 0

delta = ((0, 1), (0, -1), (1, 0), (-1, 0))

n = int(input().strip())

grid = [list(map(int, input().split())) for _ in range(n)]

shark = -1

# 아기상어 크기
level = 2

# 경험치
exp = 0

# 아기상어 초기 위치
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            shark = (i, j)

# 엄마를 부르기 전에 먹을수 있는 시간
answer = 0

# 엄마를 불러야 되면 False
mom = True

while mom:
    mom, shark = bfs(shark)

print(answer)
