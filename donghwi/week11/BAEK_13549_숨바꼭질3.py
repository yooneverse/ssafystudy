# https://www.acmicpc.net/problem/13549
from collections import deque


def bfs(start, goal):
    limit = 100001
    cnt = [-1] * limit  # 미방문: -1
    qu = deque([start])
    cnt[start] = 0  # 시작점 거리 0

    while qu:
        x = qu.popleft()
        if x == goal:
            return cnt[x]

        # 0초 간선: x -> 2x
        nx = x * 2
        if 0 <= nx < limit and cnt[nx] == -1:
            cnt[nx] = cnt[x]
            qu.appendleft(nx)

        # 1초 간선: x -> x-1, x+1
        nx = x - 1
        if 0 <= nx < limit and cnt[nx] == -1:
            cnt[nx] = cnt[x] + 1
            qu.append(nx)

        nx = x + 1
        if 0 <= nx < limit and cnt[nx] == -1:
            cnt[nx] = cnt[x] + 1
            qu.append(nx)


N, K = map(int, input().split())
print(bfs(N, K))
