# 빙고게임

# 25개 칸으로 이루어진 빙고판


# 사회자가 부르는 수를 차례로 지워나간다.

# 가로줄 세로줄 또는 대각선 위에 있는
# 5개의 모든 수가 지워지면 줄에 선 긋기
# 줄이 3개 이상이면 빙고


N = 5
matrix = [list(map(int, input().split())) for _ in range(N)]
calls = []
for _ in range(5):
    call = map(int, input().split())

visited = [0] * 26

for i in range(N):
    for j in range(N):
        visited[matrix[i][j]] = (i, j)


row = [0] * 5
col = [0] * 5
dia = [0, 0]
bingo = 0

for I, num in (1, len(calls) + 1):
    i, j = visited[num]

    row[i] += 1
    if row[i] == 5:
        bingo += 1

    col[j] += 1
    if col[j] == 5:
        bingo += 1

    if i == j:
        dia[0] += 1
        if dia[0] == 5:
            bingo += 1

    if i+j == 4:
        dia[1] +=1
        if dia[1] == 5:
            bingo += 1


    # 만약 빙고가 3이면 멈춘다.
    if bingo >=3:
        print(I)
        break
