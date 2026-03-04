import sys
input = sys.stdin.readline

N, M = map(int, input().split())

r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0

while True:

    # 현재 위치 청소
    if not visited[r][c]:
        visited[r][c] = True
        cnt += 1

    cleaned = False  # 주변에 청소할 곳 있는지 확인함

    # 왼쪽 방향부터 확인 
    for _ in range(4):

        # 왼쪽 회전
        d = (d + 3) % 4

        nx = r + dx[d]
        ny = c + dy[d]

        # 청소 안된 빈칸이면 이동함
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                r, c = nx, ny
                cleaned = True
                break

    # 이동했으면 다시 반복함
    if cleaned:
        continue

    # 네 방향 모두 청소되었으면 뒤로 이동함
    back = (d + 2) % 4
    nx = r + dx[back]
    ny = c + dy[back]

    # 뒤가 벽이면 종료
    if graph[nx][ny] == 1:
        break
    else:
        r, c = nx, ny

print(cnt)