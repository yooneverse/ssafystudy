import sys
input = sys.stdin.readline

def findhead():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '*':
                return (i, j)

def check(r, c):
    left_arm = right_arm = middle = left_leg = right_leg = 0

    tmp = 0

    # left_arm
    for i in range(N):
        if grid[r + 1][i] == '*':
            left_arm = c - i
            break

    # right_arm
    for i in range(N - 1, c - 1, -1):
        if grid[r + 1][i] == '*':
            right_arm = i - c
            break

    # middle
    for j in range(r + 1, N):
        if not middle and grid[j][c] == '_':
            middle = j - 2 - r
            tmp = j
        if middle and not left_leg and grid[j][c - 1] == '_':
            left_leg = j - tmp
        if middle and not right_leg and grid[j][c + 1] == '_':
            right_leg = j - tmp
    else:
        if not left_leg:
            left_leg = N - tmp
        if not right_leg:
            right_leg = N - tmp


    return left_arm, right_arm, middle, left_leg, right_leg

N = int(input().strip())

grid = [input().strip() for _ in range(N)]

head = findhead()

answer = check(*head)

print(head[0] + 2, head[1] + 1)
print(*answer)
