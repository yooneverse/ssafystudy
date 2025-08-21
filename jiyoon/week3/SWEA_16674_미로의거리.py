from collections import deque

# 상, 하, 좌, 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(si, sj):
    visited = [[0] * N for _ in range(N)]  # 큐 만들기
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1  # 출발점은 1로 시작 (경유 칸 수 계산 위해)

    while q:
        i, j = q.popleft()

        # 도착점을 만나면
        if maze[i][j] == 3:
            if visited[i][j] > 1:
                return visited[i][j] - 2  # 출발/도착 제외한 경유 칸 수
            else:
                return 0

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < N and 0 <= nj < N:
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:  # 벽이 아니고, 미방문한 경로
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))

    return 0  # q가 빌 때까지 도착이 불가했음을 나타냄


# 테스트 케이스 입력
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]  # 미로니까 공백 없는 입력

    found = False  # 우선 못 찾은 상황 가정
    si = sj = 0
    for i in range(N):  # 행 번호 순회
        for j in range(N):  # 열 번호 순회
            if maze[i][j] == 2:  # 출발 좌표인 2 찾기
                si, sj = i, j
                found = True  # 찾으면 종료
                break

    solve = bfs(si, sj)
    print(f"#{tc} {solve}")









