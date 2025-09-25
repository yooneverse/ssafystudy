n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]

# 네 방향 (좌, 우, 상, 하)
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# dp[x][y] = (x,y)에서 시작했을 때 최장 이동 칸 수
dp = [[0] * n for _ in range(n)]

def dfs(sx, sy):
    stack = [(sx, sy, 0)]  # (행, 열, 상태) → 상태 0=방문 시작, 1=자식 처리 후 확정
    while stack:
        x, y, state = stack.pop()
        if state == 0:
            if dp[x][y] != 0:  # 이미 계산된 칸이면 건너뜀
                continue
            stack.append((x, y, 1))  # 후처리를 위해 다시 넣음
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                # 범위 안이고, 대나무 양이 더 많아야 이동 가능
                if 0 <= nx < n and 0 <= ny < n and forest[nx][ny] > forest[x][y]:
                    if dp[nx][ny] == 0:  # 아직 이웃 미계산이면 먼저 처리
                        stack.append((nx, ny, 0))
        else:  # state == 1 → 자식들 다 처리한 뒤 확정 단계
            best = 1  # 최소 자기 자신
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and forest[nx][ny] > forest[x][y]:
                    cand = dp[nx][ny] + 1
                    if cand > best:
                        best = cand
            dp[x][y] = best

answer = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:  # 아직 계산 안 됐으면 dfs로 구함
            dfs(i, j)
        if dp[i][j] > answer:  # 전체 최댓값 갱신
            answer = dp[i][j]

print(answer)

#--------------(실패버전도 업로드합니다!)

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]

# 네 방향 (상, 하, 좌, 우)
d = [(0,-1), (0,1), (-1,0), (1,0)]

# 메모이제이션 테이블 (0 = 아직 계산 안 함)
dp = [[0] * n for _ in range(n)]

# DFS 함수
def dfs(x, y):
    if dp[x][y] != 0:              # 이미 계산된 칸이면 재활용
        return dp[x][y]

    dp[x][y] = 1                   # 최소 자기 자신 포함
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        # 이전 좌표보다 현재 좌표 값이 더 커야 함
        if 0 <= nx < n and 0 <= ny < n and forest[nx][ny] > forest[x][y]:
            value = dfs(nx, ny) + 1
            if value > dp[x][y]:
                dp[x][y] = value
    return dp[x][y]

answer = 0
for i in range(n):
    for j in range(n):
        length = dfs(i, j)
        if length > answer:
            answer = length

# 판다가 이동 가능한 칸 수의 최댓값 출력
print(answer)