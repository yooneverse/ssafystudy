from collections import deque
 
def maze_runner(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j
 
def maze(i, j, N):
    visited = [[0] * N for _ in range(N)]
    # 큐 만들어주기
    q = deque()
    # 미로의 시작을 찾아야 함
    q.append([i,j])
    # 시작점을 시작으로 q가 빌 때까지
    while q:
        # 넣엇던 인덱스 꺼내서 하나하나 실험해보자
        ni, nj = q.popleft()
        # 만약 꺼낸 인덱스가 시작점이라면 끝을내도 되겟지..
        if arr[ni][nj] == 3:
            return visited[ni][nj] -1
        # 1차원에서는 for를 써가지고 인접리스트를 확인했는데 2차원에서는 좀 달름
        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            next_i = ni + di
            next_j = nj + dj
            # 만약 범위 안에 있고 방문한 적이 없고 벽이 아니라믄
            if 0 <= next_i < N and 0 <= next_j < N and (arr[next_i][next_j] != 1) and (visited[next_i][next_j] == 0):
                # 다음 목적지에 추가
                q.append([next_i, next_j])
                visited[next_i][next_j] = visited[ni][nj] + 1
        # 경로 없는 경우에
    return 0
 
 
T = int(input())
for tc in range(1, T+1):
    # 2차원 배열 크기
    N = int(input())
    # 내가 받는 2차원 배열
    arr = [list(map(int, input())) for _ in range(N)]
 
    sti, stj = maze_runner(N)
    answer = maze(sti, stj, N)
    print(f'#{tc} {answer}')