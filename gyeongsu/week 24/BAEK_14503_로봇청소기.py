n, m = map(int, input().split())

r, c, dir = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

visited = [[False] * m for _ in range(n)]

if dir == 0:
    move_r, move_c = -1, 0
elif dir == 1:
    move_r, move_c = 0, 1
elif dir == 2:
    move_r, move_c = 1, 0
else:
    move_r, move_c = 0, -1

n_clean = 0
stop = True
while stop:
    # print(r, c, move_r, move_c)
    if matrix[r][c] == 0 and not visited[r][c]:
        n_clean += 1
        matrix[r][c] = 2
        visited[r][c] = True

    all_clean = True
    for dr, dc in (zip([1,-1,0,0], [0,0,1,-1])):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and not (matrix[nr][nc] == 1):
            if matrix[nr][nc] == 0: # 작동 3
                all_clean = False #
                break

    if all_clean:
        r, c = r - move_r , c - move_c
        if matrix[r][c] == 1:
            stop = False
    else:
        move_r, move_c = - move_c, move_r # 반시계 90도 회전
        if matrix[r + move_r][c + move_c] == 0:
            r, c = r + move_r, c + move_c

print(n_clean)