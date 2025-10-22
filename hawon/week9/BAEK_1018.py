# TODO : 지민이가 칠해야 하는 정사각형의 최소 개수
# 8x8 크기로 판별하기

# N M 크기의 보드
N,M = map(int, input().split())
# B 검은색, W 흰색
board = [list(input()) for _ in range(N)]

def chess(x, y):
    pattern = ['BWBWBWBW', 'WBWBWBWB']

    count_W = 0  # 왼쪽 위가 W인 경우
    count_B = 0  # 왼쪽 위가 B인 경우

    # 8방향 탐색
    for i in range(8):
        for j in range(8):
            now_color = board[x + i][y + j]  # 현재 칸의 색상

            # W로 시작
            # 짝수 행은 "WBWBWBWB", 홀수 행은 "BWBWBWBW"가 되어야 함
            if now_color != pattern[i % 2][j]:
                count_W += 1
            # B로 시작
            if now_color != pattern[(i + 1) % 2][j]:
                count_B += 1

    return min(count_W, count_B)

min_val = float('inf')

# 시작 좌표는 (0~N-8, 0~M-8)까지만 가능
for i in range(N - 7): 
    for j in range(M - 7): 
        now_val = chess(i, j)
        min_val = min(min_val, now_val)
    
print(min_val)