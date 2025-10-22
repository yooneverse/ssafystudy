C, R = map(int, input().split())

K = int(input().strip())

if K > C * R:
    print(0)
else:
    dirs = True
    col = [C - 1, 0]
    row = [R, 0]
    answer = [1, 0]
    cnt = 0
    for i in range(1, C * R + 1):
        cnt += 1
        if dirs:
            answer[1] += 1 - 2 * row[1]
            if row[0] == cnt:
                cnt = 0
                dirs = False
                row[0] -= 1
                row[1] = 1 - row[1]
        else:
            answer[0] += 1 - 2 * col[1]
            if col[0] == cnt:
                cnt = 0
                dirs = True
                col[0] -= 1
                col[1] = 1 - col[1]
        if i == K:
            break
    print(*answer)
