# BAEK 1245. 농장 관리
# BFS, deque 사용
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
# 상하좌우 + 대각 delta 배열
d = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]

# 산봉우리: 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합
# 인접하다: X좌표 차이, Y좌표 차이 모두 1 이하
# 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작음

# 방문 배열 생성
visited = [[0] * M for _ in range(N)]

# 산봉우리 탐색 함수 정의
def mountain(row, col):
    q = deque([(row, col)])
    visited[row][col] = 1
    bong = True     # 산봉우리인지 아닌지 판별

    # deque 반복
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            # 범위 설정
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            # 주변이 더 크면 산봉우리 아님
            if grid[nr][nc] > grid[r][c]:
                bong = False
            # 방문 여부 확인
            if visited[nr][nc]:
                continue
            # 다음 방문지 저장
            elif grid[nr][nc] == grid[r][c]:
                q.append((nr, nc))
                visited[nr][nc] = 1

    if bong:
        # 봉우리로 지정된 좌표 확인
        visited[r][c] = 'X'
        return 1
    else:
        return 0


ans = 0

# 방문하지 않은 좌표 i, j를 산봉우리 탐색 함수의 전달인자로 사용
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            ans += mountain(i, j)

# 봉우리가 어디있나
# for arr in visited:
#   print(arr)
print(ans)
