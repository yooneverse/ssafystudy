# import sys
# sys.stdin = open("input.txt", "r")



for _ in range(10):
    tc = int(input().strip())
    N = 100

    # 1) 100×100 행렬 입력
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    # 2) 각 행의 합
    for i in range(N):
        total = 0
        for j in range(N):
            total += matrix[i][j]
        if total > max_sum:       # 각 행의 합이 최댓값을 넘으면 최댓값이 된다. 
            max_sum = total

    # 3) 각 열의 합
    for j in range(N):
        total = 0
        for i in range(N):
            total += matrix[i][j] # 각 열의 합이 최댓값을 넘으면 최댓값이 된다. 
        if total > max_sum:
            max_sum = total

    # 4) 우하향 대각선 합 (i,i)  
    diag1 = 0
    for i in range(N):
        diag1 += matrix[i][i]          # 우하향 대각선은 (0,0)을 기준으로 (i, i)씩 늘어난다. 
    if diag1 > max_sum:                #우하향 대각선의 합이 최댓값을 넘으면 최댓값이 된다. 
        max_sum = diag1

    # 5) 우상향 대각선 합 (i, N-1-i) 
    diag2 = 0
    for i in range(N):
        diag2 += matrix[i][N-1-i]      # 우하향 대각선은 (0,0)을 기준으로 (i , N-1-i)씩 늘어난다. 
    if diag2 > max_sum:                #우상향 대각선의 합이 최대값을 넘으면 최댓값이 된다.
        max_sum = diag2

    # 6) 결과 출력 (“#번호 값” 형식)    
    print(f'#{tc} {max_sum}')