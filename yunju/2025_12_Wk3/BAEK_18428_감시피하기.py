import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
board = [list(input().split()) for _ in range(N)]

teachers = []
empty = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            teachers.append((i, j))
        elif board[i][j] == 'X':
            empty.append((i, j))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def watch():
    for x, y in teachers:
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break
                if board[nx][ny] == 'O':
                    break
                if board[nx][ny] == 'S':
                    return False
    return True

found = False
# 빈 공간 중 장애물을 둘 세 곳
for comb in combinations(empty, 3):
    for x, y in comb:
        board[x][y] = 'O'

    if watch():
        found = True
    for x, y in comb:
        board[x][y] = 'X'

    if found:
        break

if found:
    print("YES")
else:
    print("NO")