# 빈 보드 만들어주기
board = [[0] * 100 for _ in range(100)]


# 입력받으면서 보드에 색칠해주기
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1,x2):
        for j in range(y1,y2):
            board[i][j] = 1

total = 0

for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            total += 1

print(total)