from collections import deque
# 시작점 정하기
def maze_runner(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                return i, j

def maze_exit(i, j, N):
    # visited 배열
    visited = [[0] * N for _ in range(N)]
    # q 만들기
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        si, sj = q.popleft()

        # 만약에 꺼낸 좌표가 출발점이면 좌표 반환
        if maze[si][sj] == 2:
            return 1
        # 상하좌우로 탐색 ㄱㄱ
        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni = si+di
            nj = sj+dj
            # 이게 범위 안이고, 벽이 아니고,
            if 0 <= ni < N and 0 <= nj < N and (maze[ni][nj] != 1) and (visited[ni][nj] == 0):
                q.append([ni,nj])
                visited[ni][nj] = visited[si][sj] + 1
    return 0

T = 10
for tc in range(1, T+1):
    t = input()
    # 미로는 16x16
    maze = [list(map(int, input())) for _ in range(16)]
    N = 16

    sti, stj = maze_runner(N)
    answer = maze_exit(sti, stj, N)
    print(f'#{tc} {answer}')