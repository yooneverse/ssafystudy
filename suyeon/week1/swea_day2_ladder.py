def find_destination_idx(arr):
    last_row = arr[-1]
    for i in range(len(last_row)):
        if last_row[i] == 2:
            return i
 
 
T = 10
for test_case in range(1, T + 1):
    ts = int(input())
    minimap = [list(map(int, input().split())) for _ in range(100)]
 
    # 현재 위치 = X, 거꾸로 올라갈 예정
    cx = 99
    cy = find_destination_idx(minimap)
 
    # cx = 0, 제일 위까지 올라옴
    while cx > 0:
        # 왼쪽에 통로 존재
        if 0 <= cy - 1 < 100 and minimap[cx][cy - 1] == 1:
            # 0에 막히기 전까지 왼쪽으로 이동
            while True:
                ny = cy - 1
                if 0 <= ny < 100 and minimap[cx][ny] == 1:
                    minimap[cx][cy] = 0  # 지나간 길 막기
                    cy = ny
                else:
                    break
                    
        # 오른쪽에 통로 존재
        elif 0 <= cy + 1 < 100 and minimap[cx][cy + 1] == 1:
            # 0에 막히기 전까지 오른쪽으로 이동
            while True:
                ny = cy + 1
                if 0 <= ny < 100 and minimap[cx][ny] == 1:
                    minimap[cx][cy] = 0  # 지나간 길 막기
                    cy = ny
                else:
                    break
        # 위로 직진
        minimap[cx][cy] = 0
        cx -= 1
 
    print(f'#{test_case} {cy}')