from collections import deque

# 상, 하, 좌, 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj):
    # 방문 여부를 기록
    visited = [[0] * N for _ in range(N)]
    # 큐 생성
    q = deque()
    # 출발 좌표 큐에 삽입
    q.append((si, sj))
    # 출발 좌표 방문 처리
    visited[si][sj] = 1

    while q:
        # 큐에서 현재 좌표 꺼내기
        i, j = q.popleft()

        # 현재 위치가 도착점인 3인지 확인
        if maze[i][j] == 3:
            return 1  # 도달했으면 1 반환

        # 상하좌우 네 방향으로 이동
        for d in range(4):
            ni = i + di[d]  # 행 이동
            nj = j + dj[d]  # 열 이동

            # 새로운 좌표가 미로 범위 안에 있는지 확인
            if 0 <= ni < N and 0 <= nj < N:
                # 벽이 아니고, 아직 방문하지 않은 경우
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    # 현재 좌표의 거리 + 1 기록
                    visited[ni][nj] = visited[i][j] + 1
                    # 다음 탐색 대상 큐에 삽입
                    q.append((ni, nj))

    # 도달 불가능
    return 0


# 총 10개의 테스트케이스
T = 10
for _ in range(T):
    tc = int(input())  # 테스트케이스 번호
    N = 16
    maze = [list(map(int, input().strip())) for _ in range(N)]

    # 우선 못 찾은 상황 가정
    found = False
    si = sj = 0
    # 미로 전체를 순회하며 출발 좌표인 2 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # 출발 좌표 2 발견
                si, sj = i, j  # 좌표 저장
                found = True  # 찾음 표시
                break
            if found:
                break

    solve = bfs(si, sj)
    print(f"#{tc} {solve}")
