import sys
input = sys.stdin.readline

from collections import deque

def bfs(floor, start):
    visited = [0] * (n + 1)
    visited[start] = 1

    que = deque()
    que.append(start)

    answer = 0

    while que:
        node = que.popleft()

        for nxt, d in usado[node]:
            if d < floor:
                continue
            if visited[nxt]:
                continue
            visited[nxt] = 1
            que.append(nxt)
            answer += 1
    return answer


n, q = map(int, input().split())

usado = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    s, e, r = map(int, input().split())
    usado[s].append((e, r))
    usado[e].append((s, r))

for _ in range(q):
    k, v = map(int, input().split())
    print(bfs(k, v))
