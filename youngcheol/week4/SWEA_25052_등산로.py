T = int(input())

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0  # 가장 긴 등산로의 길이 

    for i in range(N):         # 전체 등산로 
        for j in range(N):
            ci, cj, = i, j     # 시작점
            len = 1             # 길이는 1부터 시작 

            while True:
                mini, minj = ci, cj       #최저점
                for d in range(4):       #갈 수 있는 범위가 상하좌우
                    ni = ci + di[d]  
                    nj = cj + dj[d]


                        # 만약 범위안에 들어오고 matrix[ni][nj]이 matrix[mini][minj]보다 작으면 최저점이 바뀐다
                    if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] < matrix[mini][minj]:
                        mini, minj = ni, nj             
                if (mini,minj) == (ci, cj):   #더 이상 갈 곳이 없을 때 멈춘다
                    break
                ci, cj = mini, minj
                len += 1

            if max_v < len:
                max_v = len



    print(f'#{tc} {max_v}')