def roll_ball(arr, arr_size, start_x, start_y):
    roll_num = 1
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    already_go = [[0] * arr_size for _ in range(arr_size)]
    while True:
        min_num = arr[start_x][start_y]
        min_direction = []
        already_go[start_x][start_y] = 1
        for dx, dy in direction:
            nx = start_x + dx
            ny = start_y + dy
            if 0 <= nx < arr_size and 0 <= ny < arr_size and already_go[nx][ny] == 0:
                if min_num > arr[nx][ny]:
                    min_num = arr[nx][ny]
                    min_direction = [dx, dy]
 
        if not min_direction:
            return roll_num
 
        start_x += min_direction[0]
        start_y += min_direction[1]
        roll_num += 1
    return roll_num
 
 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    board_size = int(input())
    board = [list(map(int, input().split())) for _ in range(board_size)]
 
    max_roll = 0
    for i in range(board_size):
        for j in range(board_size):
            roll = roll_ball(board, board_size, i, j)
            if max_roll < roll:
                max_roll = roll
 
    print(f'#{test_case} {max_roll}')