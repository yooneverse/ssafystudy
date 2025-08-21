from collections import deque

def bfs(si, sj):
    visited = [[0]*N for _ in range(N)]

    q = deque()  # 다음에 갈 장소 저장
    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        i, j = q.popleft()  # deque는 popleft 사용
        if matrix[i][j] == 3:  # 꺼낸 좌표가 도착지이면
            return visited[i][j] - 2  # 출발(2)과 도착(3)을 빼고 그 사이 0의 개수

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            # 벽이 1인 지점 통과 불과, 아직 방문하지 않은 칸인지 확인,
            if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    return 0  # 경로가 없는 경우

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())         # 미로의 크기
    matrix = [list(map(int, input().strip())) for _ in range(N)]

    # 출발지 2 찾기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:       #2에서 출발하니까 값이 2인 지점이 시작점
                si, sj = i, j

    print(f'#{tc} {bfs(si, sj)}')