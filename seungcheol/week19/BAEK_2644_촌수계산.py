import sys
input = sys.stdin.readline

from collections import deque

n = int(input().strip())

a, b = map(int, input().split())

m = int(input().strip())

edge = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    edge[s].append(e)
    edge[e].append(s)

def bfs(start, end):
    que = deque([(start, 0)])
    visited = [0] * (n + 1)

    while que:
        node, level = que.popleft()

        for nxt in edge[node]:
            if nxt == end:
                return level + 1

            if visited[nxt]:
                continue

            visited[nxt] = 1
            que.append((nxt, level + 1))

    return -1

answer = bfs(a, b)
print(answer)
