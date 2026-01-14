N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
result = []

for i in range(N - 7):
    for j in range(M - 7):
        cnt_1 = 0
        cnt_2 = 0
        for y in range(i, i + 8):
            for x in range(j, j + 8):
                if (y + x) % 2 == 0:
                    if board[y][x] != 'B':
                        cnt_1 += 1
                    elif board[y][x] != 'W':
                        cnt_2 += 1
                else:
                    if board[y][x] != 'W':
                        cnt_1 += 1
                    elif board[y][x] != 'B':
                        cnt_2 += 1
        result.append(cnt_1)
        result.append(cnt_2)

print(min(result))
