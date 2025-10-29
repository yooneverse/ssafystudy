# BAEK 12100. 2048 (Easy)
import sys
sys.stdin = open('input.txt', 'r')
from copy import deepcopy

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


def cal(arr):
    before = [x for x in arr if x]
    after = []
    c = 0
    while c < len(before):
        if c == len(before) - 1:
            after.append(before[c])
            break
        if before[c] == before[c + 1]:
            after.append(before[c] * 2)
            c += 2
        else:
            after.append(before[c])
            c += 1

    after += [0] * (N - len(after))
    return after


# dirs = (0: 상, 1: 하, 2: 좌, 3: 우)
def moving(dirs, grid):
    if dirs == 0:
        for j in range(N):
            col = [grid[i][j] for i in range(N)]
            col = cal(col)
            for i in range(N):
                grid[i][j] = col[i]

    elif dirs == 1:
        for j in range(N):
            col = [grid[i][j] for i in range(N)]
            col = cal(col[::-1])[::-1]
            for i in range(N):
                grid[i][j] = col[i]

    elif dirs == 2:
        for i in range(N):
            grid[i] = cal(grid[i])

    else:
        for i in range(N):
            grid[i] = cal(grid[i][::-1])[::-1]
    ans = 0
    for arr in grid:
        ans = max(ans, max(arr))
    return ans


def backtrack(cnt, g, res):
    global max_block

    if cnt == 5:
        max_block = max(max_block, res)
        return

    for i in range(4):
        mat = deepcopy(g)
        ans = moving(i, mat)
        backtrack(cnt + 1, mat, ans)


max_block = 0
backtrack(0, matrix, 0)
print(max_block)
