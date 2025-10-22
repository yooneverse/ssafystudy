def check(num):
    for i in range(5):
        for j in range(5):
            if cheolsu[i][j] == num:
                cheolsu[i][j] = 0
                return


def bingo():
    line = 0
    # 대각선
    for k in range(2):
        tmp = 0
        for i in range(5):
            if not cheolsu[i][4 * k + i - 2 * k * i]:
                tmp += 1
                if tmp == 5:
                    line += 1
            else:
                break
    # 가로
    for i in range(5):
        row = 0
        col = 0
        for j in range(5):
            if not cheolsu[i][j]:
                row += 1
                if row == 5:
                    line += 1
            else:
                break
        for k in range(5):
            if not cheolsu[k][i]:
                col += 1
                if col == 5:
                    line += 1
            else:
                break

    return line


cheolsu = [list(map(int, input().split())) for _ in range(5)]

number = [list(map(int, input().split())) for _ in range(5)]

cnt = 0

for i in range(5):
    for j in range(5):
        check(number[i][j])
        cnt += 1
        if cnt < 12:
            continue

        if bingo() >= 3:
            print(cnt)
            exit()