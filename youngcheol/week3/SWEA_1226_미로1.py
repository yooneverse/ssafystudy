from collections import deque
#상하좌우 배열
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N = 16  # 16x16 고정

def bfs(si, sj):
    visited = [[0]*N for _ in range(N)]  
    q = deque()          #다음에 방문할 곳 저장
    q.append((si, sj))    # 이차원 배열보니 변수 두개로 저장
    visited[si][sj] = 1    

    while q:
        i, j = q.popleft()       

        # 도착지면 1 반환    # 문제에서 도달 가능하면 1로 나타내라했음
        if matrix[i][j] == 3:
            return 1

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            # 1이면 벽이라 방문 불가 , 방문하지않은 곳 방문 
            if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] != 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))

    # 도달 불가
    return 0

# 총 10개 테스트 케이스
for _ in range(10):
    tc = int(input().strip())
    matrix = [list(map(int, input().strip())) for _ in range(N)]

    # 출발지(2) 찾기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:       #2에서 출발하니까 값이 2인 지점이 시작점
                si, sj = i, j

    print(f'#{tc} {bfs(si, sj)}')