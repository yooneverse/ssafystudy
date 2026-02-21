import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
rooms = [input().strip() for _ in range(N)]

change_cnt = [[float('inf')] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solve():
    q = deque([(0, 0, 0)])
    change_cnt[0][0] = 0

    while q:
        x, y, cnt = q.popleft()

        if x == N - 1 and y == N - 1:
            return cnt

        if change_cnt[x][y] < cnt:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                # 흰 방인 경우 (비용 0)
                if rooms[nx][ny] == '1':
                    if change_cnt[nx][ny] > cnt:
                        change_cnt[nx][ny] = cnt
                        q.appendleft((nx, ny, cnt))
                # 검은 방인 경우 (비용 1)
                else:
                    if change_cnt[nx][ny] > cnt + 1:
                        change_cnt[nx][ny] = cnt + 1
                        q.append((nx, ny, cnt + 1))

print(solve())