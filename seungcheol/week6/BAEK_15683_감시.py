# gpt 풀이
N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# 상 우 하 좌
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# cctv 별 감시 방향
cctv_dirs = {1: [[0], [1], [2], [3]],
             2: [[0, 2], [1, 3]],
             3: [[0, 1], [1, 2], [2, 3], [3, 0]],
             4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
             5: [[0, 1, 2, 3]]
             }

# cctv 위치
cctv = []

# cctv 위치 저장
for i in range(N):
    for j in range(M):
        # 5는 경우가 1가지이므로 바로 저장
        if graph[i][j] == 5:
            for d in cctv_dirs[5][0]:
                ni = i + delta[d][0]
                nj = j + delta[d][1]
                while 0 <= ni < N and 0 <= nj < M:
                    if graph[ni][nj] == 6:
                        break
                    if not graph[ni][nj]:
                        graph[ni][nj] = -1
                    ni += delta[d][0]
                    nj += delta[d][1]
        # cctv 위치 저장
        elif 1 <= graph[i][j] <= 4:
            cctv.append((i, j, graph[i][j]))

# 공백 지역 수
answer = float("inf")


# cctv 감시지역 마킹
def watch(matrix, r, c, dirs):
    # 원복에 필요한 감시지역 위치
    change = []

    # cctv 감시지역 수만큼 반복
    for d in dirs:
        nr, nc = r, c
        while 0 <= nr < N and 0 <= nc < M:
            if matrix[nr][nc] == 6:
                break
            if not matrix[nr][nc]:
                matrix[nr][nc] = -1
                change.append((nr, nc))
            nr += delta[d][0]
            nc += delta[d][1]
    return change

# dfs, cctv 감시 경우의 수 모두 확인
def dfs(matrix, idx):
    global answer

    # cctv 전부 확인 시 공백구역 최소값 최신화
    if idx == len(cctv):
        cnt = sum(row.count(0) for row in matrix)
        answer = min(answer, cnt)
        return

    r, c, s = cctv[idx]

    for dirs in cctv_dirs[s]:
        change = watch(matrix, r, c, dirs)
        dfs(matrix, idx + 1)

        # 원복
        for y, x in change:
            matrix[y][x] = 0


dfs(graph, 0)

print(answer)

# 최초 풀이
import copy

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# 상 우 하 좌
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

cctv = []

for i in range(N):
    for j in range(M):
        # 5는 미리 적용
        if graph[i][j] == 5:
            for d in range(4):
                ni = i + delta[d][0]
                nj = j + delta[d][1]
                while 0 <= ni < N and 0 <= nj < M:
                    if not graph[ni][nj]:
                        graph[ni][nj] = "#"
                    if graph[ni][nj] == 6:
                        break
                    ni += delta[d][0]
                    nj += delta[d][1]
        # 다른 cctv 저장
        elif graph[i][j] in [1, 2, 3, 4]:
            cctv.append((i, j, graph[i][j]))

# 최대 공백 수
answer = float("inf")

# 방 정보, cctv 위치, cctv 적용 수
def dfs(matrix, camera, idx):
    global answer

    # cctv 모두 적용 시
    if idx == len(camera):
        cnt = 0
        for y in range(N):
            for x in range(M):
                if not matrix[y][x]:
                    cnt += 1
        # cctv 수 최신화
        answer = min(answer, cnt)
        return

    # cctv 정보
    r, c, s = camera[idx]

    if s == 1:
        for k in range(4):
            tmp = copy.deepcopy(matrix)
            nr = r + delta[k][0]
            nc = c + delta[k][1]
            while 0 <= nr < N and 0 <= nc < M:
                if not tmp[nr][nc]:
                    tmp[nr][nc] = "#"
                if tmp[nr][nc] == 6:
                    break
                nr += delta[k][0]
                nc += delta[k][1]
            dfs(tmp, camera, idx + 1)

    elif s == 2:
        for k in range(2):
            tmp = copy.deepcopy(matrix)
            nr = r + delta[k][0]
            nc = c + delta[k][1]
            while 0 <= nr < N and 0 <= nc < M:
                if not tmp[nr][nc]:
                    tmp[nr][nc] = "#"
                if tmp[nr][nc] == 6:
                    break
                nr += delta[k][0]
                nc += delta[k][1]

            nr = r + delta[k + 2][0]
            nc = c + delta[k + 2][1]
            while 0 <= nr < N and 0 <= nc < M:
                if not tmp[nr][nc]:
                    tmp[nr][nc] = "#"
                if tmp[nr][nc] == 6:
                    break
                nr += delta[k + 2][0]
                nc += delta[k + 2][1]
            dfs(tmp, camera, idx + 1)

    elif s == 3:
        for k in range(4):
            tmp = copy.deepcopy(matrix)
            nr = r + delta[k][0]
            nc = c + delta[k][1]
            while 0 <= nr < N and 0 <= nc < M:
                if not tmp[nr][nc]:
                    tmp[nr][nc] = "#"
                if tmp[nr][nc] == 6:
                    break
                nr += delta[k][0]
                nc += delta[k][1]

            k = (k + 1) % 4
            nr = r + delta[k][0]
            nc = c + delta[k][1]
            while 0 <= nr < N and 0 <= nc < M:
                if not tmp[nr][nc]:
                    tmp[nr][nc] = "#"
                if tmp[nr][nc] == 6:
                    break
                nr += delta[k][0]
                nc += delta[k][1]
            dfs(tmp, camera, idx + 1)

    elif s == 4:
        for k in range(4):
            tmp = copy.deepcopy(matrix)
            nr = r + delta[k][0]
            nc = c + delta[k][1]
            while 0 <= nr < N and 0 <= nc < M:
                if not tmp[nr][nc]:
                    tmp[nr][nc] = "#"
                if tmp[nr][nc] == 6:
                    break
                nr += delta[k][0]
                nc += delta[k][1]

            k = (k + 1) % 4
            nr = r + delta[k][0]
            nc = c + delta[k][1]
            while 0 <= nr < N and 0 <= nc < M:
                if not tmp[nr][nc]:
                    tmp[nr][nc] = "#"
                if tmp[nr][nc] == 6:
                    break
                nr += delta[k][0]
                nc += delta[k][1]

            k = (k + 1) % 4
            nr = r + delta[k][0]
            nc = c + delta[k][1]
            while 0 <= nr < N and 0 <= nc < M:
                if not tmp[nr][nc]:
                    tmp[nr][nc] = "#"
                if tmp[nr][nc] == 6:
                    break
                nr += delta[k][0]
                nc += delta[k][1]

            dfs(tmp, camera, idx + 1)

dfs(graph, cctv, 0)

print(answer)
