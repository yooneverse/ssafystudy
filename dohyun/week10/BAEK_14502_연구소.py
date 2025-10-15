# BAEK 14502. 연구소
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
d = (0, 1), (0, -1), (1, 0), (-1, 0)


def BFS(walls):
    global best
    q = deque()
    visited = [[False] * M for _ in range(N)]
    cnt = 0

    for vr, vc in viruses:
        q.append((vr, vc))
        visited[vr][vc] = True

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                # 원래 벽이거나 우리가 세운 벽이면 전파 불가
                if grid[nr][nc] == 1 or (nr, nc) in walls:
                    continue
                visited[nr][nc] = True
                q.append((nr, nc))
                if grid[nr][nc] == 0:
                    cnt += 1
                    # 가능한 안전영역이 현재 best 이하라면 더 이상 의미 없음
                    if max_best - cnt <= best:
                        return

    safe_area = max_best - cnt
    if safe_area > best:
        best = safe_area

    # 전체 최대치에 도달하면 완전 종료
    if best == max_best:
        return


safes = []
viruses = []
sum_safes = best = 0

for r in range(N):
    for c in range(M):
        if grid[r][c] == 0:
            safes.append((r, c))
            sum_safes += 1
        elif grid[r][c] == 2:
            viruses.append((r, c))

max_best = sum_safes - 3
s = len(safes)
for i in range(s - 2):
    if best == max_best:
        break
    a = safes[i]
    for j in range(i + 1, s - 1):
        if best == max_best:
            break
        b = safes[j]
        for k in range(j + 1, s):
            c = safes[k]
            w = {a, b, c}
            BFS(w)

print(best)