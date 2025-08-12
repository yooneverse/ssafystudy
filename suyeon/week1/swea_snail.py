T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
 
    cx = cy = 0
    step = 1
    snail[cx][cy] = step
 
    idx = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while step < n * n:
        nx = cx + dx[idx]
        ny = cy + dy[idx]
        if 0 <= nx < n and 0 <= ny < n:
            if snail[nx][ny] == 0:
                step += 1
                snail[nx][ny] = step
                cx = nx
                cy = ny
            else:
                idx += 1
                idx %= 4
 
        else:
            idx += 1
 
    print(f'#{test_case}')
    for row in snail:
        print(*row)