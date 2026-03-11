# 1 X 1 X 1  크기의 블록


# 세로 N 가로 M 집터
# 집터 내의 땅 높이를 똑같이 만들기
# B는 인벤토리 있는 블록개수
N, M, B = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

# 1. 좌표(i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다

# 2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.

# 1번작업은 2초 2번작업은 1초 소요

cnt = float('inf') # 처음에 0으로 답이 안나와서 보니까 0으로하면 갱신이 안되서 이걸 쓰라고 하더라고요
ans_h = 0           # 정답 높이 저장

#모든 땅의 높이 탐색
for h in range(257):
    remove = 0
    add = 0
    
    for i in range(N):
        for j in range(M):
            diff = matrix[i][j] - h
            if diff > 0:
                remove += diff  # 목표보다 높으면 없애자
            else:
                add -= diff     # 목표보다 낮으면 더하자
                
    # 인벤토리에 있는지 확인해봐 ( 여기서 제미나이씀)
    if remove + B >= add:
        time = (remove * 2) + add
        
        # 최소 시간(cnt) 갱신 (시간이 같으면 더 높은 높이 선택)
        if time <= cnt:
            cnt = time
            ans_h = h

print(cnt, ans_h)