# 상하좌우 대각선으로 땅을 갈 수 있으면 같은 섬

# 상하좌우 , 우상, 우하, 좌하, 좌상
di = [-1, 1, 0, 0, -1, 1, 1, -1]
dj = [0, 0, -1, 1, 1, 1, -1, -1]






# 1은 땅 0은 바다

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:  # 만약 너비랑 높이랑 0이면 중단
        break
    # 너비 w
    # 높이 h
    matrix = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    cnt = 0  # 섬의 개수
    for i in range(h):  # 사각형의 범위
        for j in range(w):
            if matrix[i][j] == 1 and not visited[i][j]:  # 방문한적 없고 방문한 곳이 땅이면
                cnt += 1            # 1 증가
                stack = [(i, j)]
                visited[i][j] = 1   # 방문처리

            # 다음 섬
                while stack:
                    x, y = stack.pop()
                    for d in range(8): #8방향
                        nx = x + di[d]
                        ny = y + dj[d]

                        if 0 <= nx < h and 0 <= ny < w:  # 범위
                            if matrix[nx][ny] == 1 and not visited[nx][ny]:  # 방문한적 없고 방문한 곳이 땅이면
                                visited[nx][ny] = 1 #방문처리
                                stack.append((nx, ny))

    print(cnt)
