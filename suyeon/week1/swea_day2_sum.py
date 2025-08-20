def maxsum_of_row(num_arr):
    cur_row = 0
    max_row = 0
    for i in range(100):
        for j in range(100):
            cur_row += num_arr[i][j]
 
        if max_row < cur_row:
            max_row = cur_row
 
        cur_row = 0
    return max_row
 
 
def maxsum_of_column(num_arr):
    cur_col = 0
    max_col = 0
    for i in range(100):
        for j in range(100):
            cur_col += num_arr[j][i]
 
        if max_col < cur_col:
            max_col = cur_col
 
        cur_col = 0
 
    return max_col
 
 
def sum_of_left2right(num_arr):
    sum_lr = 0
    for i in range(100):
        sum_lr += num_arr[i][i]
    return sum_lr
 
 
def sum_of_right2left(num_arr):
    sum_rl = 0
    for i in range(100):
        sum_rl += num_arr[i][100 - 1 - i]
    return sum_rl
 
 
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test_num = int(input())
 
    # 입력받기
    arr = [list(map(int, input().split())) for _ in range(100)]
 
    row = maxsum_of_row(arr)
    col = maxsum_of_column(arr)
    lr = sum_of_left2right(arr)
    rl = sum_of_right2left(arr)
 
    print(f'#{test_num} {max(row,col,lr,rl)}')