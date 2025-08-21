from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj):

    visited = [[0] * N for _ in range(N)]
    # range(N)에서 range의 범위가 N인지 N+1인지 헷갈립니다.

    q = deque()    # 다음에 방문할 장소 저장

    q.append(si, sj)  #시작 장소를 큐에 추가하고

    visited[si, sj] = 1  # 시작점을 1로 해서 진행

    while q:      #while문을 언제 쓰면 좋은지 팁같은거 있는지 궁금합니다.
        i, j = q.popleft()

        if maze[i][j] == 3:           #만약 maze[i][j]가 값이 3이면
            return visited[i][j]        # visited[i][j]값 반환


        for d in range(4):
            ni = i + di[d]    #다음칸으로 1칸씩 상하좌우로 움직이고
            nj = j + dj[d]    # 움직일때마다 새로운 좌표생성




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]
    adj_l = [[] for _ in range(N+1)] #인접리스트