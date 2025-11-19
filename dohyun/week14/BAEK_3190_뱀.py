# BAEK 3190. 뱀
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

# 입력부
N = int(input())
grid = [[0] * N for _ in range(N)]
grid[0][0] = 1  # 뱀: 1
bodies = deque([(0, 0)])

# 사과 위치
K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    grid[row - 1][col - 1] = 2  # 사과: 2

# 방향 전환
L = int(input())
moves = []
for _ in range(L):
    X, C = map(str, input().split())
    moves.append((X, C))

# 1) 사과를 먹으면 뱀 길이가 늘어남
# 2) 상하좌우 벽 => 델타
# 3) 게임 시작 시 뱀은 맨 위 맨 좌측에 위치, 길이는 1, 방향은 오른쪽
# 4) 뱀 이동 규칙
#   1. 몸 길이를 늘려 머리를 다음칸에 위치시킴
#   2. 벽이나 자기 자신의 몸과 부딪히면 게임 종료
#   3. 이동한 칸에 사과가 있다면 사과가 없어지고 꼬리는 움직이지 않음
#   4. 없다면 몸길이를 줄여서 꼬리가 위치한 칸을 줄임. (몸길이 유지)


# 방향 전환 함수
# R, L 두 가지
def turn(direction, delta):
    if direction == 'D':
        if delta[0] == 0:
            return delta[1], delta[0]
        else:
            return -delta[1], -delta[0]
    else:
        if delta[0] == 0:
            return -delta[1], -delta[0]
        else:
            return delta[1], delta[0]


# 이동 함수
# (y, x): 머리 위치, d: 이동 방향(dirs[n])
def move_str(y, x, d):
    ny, nx = y + d[0], x + d[1]
    if ny < 0 or ny >= N or nx < 0 or nx >= N:
        return -1, -1
    # 사과를 안 먹었을 때는 꼬리 위치를 비워준다.
    if grid[ny][nx] == 0:
        by, bx = bodies.popleft()
        grid[by][bx] = 0
    # 늦게 확인하는 이유:
    # 머리가 꼬리를 향할 때 꼬리를 먼저 빼주고 머리가 들어갈 수 있기 때문
    if grid[ny][nx] == 1:
        return -1, -1
    bodies.append((ny, nx))
    grid[ny][nx] = 1
    return ny, nx


def game():
    t = 0   # 총 게임 시간
    r = c = 0   # 최초 위치
    d = (0, 1)  # 최초 시작 시 오른쪽으로 이동
    moves_i = 0
    # 이동 시작
    while (r, c) != (-1, -1) and moves_i < len(moves):
        r, c = move_str(r, c, d)
        t += 1
        if t == int(moves[moves_i][0]):
            d = turn(moves[moves_i][1], d)
            moves_i += 1
    # for cnt, change in moves:
    #     cnt = int(cnt)
    #     loop_cnt = 0
    #     while loop_cnt < cnt:
    #         r, c = move_str(r, c, d)
    #         loop_cnt += 1
    #         if (r, c) == (-1, -1):
    #             print(t + loop_cnt)
    #             return
    #     t += loop_cnt
    #     d = turn(change, d)
    while (r, c) != (-1, -1):
        r, c = move_str(r, c, d)
        t += 1
    print(t)


game()
