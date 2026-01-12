# 정사각형 내부에서만 움직일 수 있다.
# 출발점은 항상 정사격형의 가장 왼쪽
# 젤리가 이동 가능한 방향은 오른쪽과 아래 뿐
# 위쪽이랑 왼쪽으로 이동불가
# 가장 오른쪽, 가장 아래칸에 이동한 순간 게임 종료
# 한번에 이동할 수 있는 칸은 밟고 잇는 수만큼

di = [0, 1]
dj = [1, 0]

# 정사각형 가로 세로의 길이
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 출발점 0,0
si, sj = (0, 0)
for i in range(N):
    for j in range(N):
        jump = matrix[i][j]

        if jump == 0:
            continue

        for d in range(2):
            ni = si + di[d] * jump
            nj = sj + dj[d] * jump
            if 0 <= ni < N and 0 <= nj < N:
                si, sj = ni, nj

# 끝점에 도달하면 HaruHaru
if matrix[si][sj] == -1:
    print('HaruHaru')
# 도달 불가면 Hing
else:
    print('Hing')
