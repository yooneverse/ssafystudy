# 최초 풀이: bfs는 O(N)
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, end):
    if start == end:
        return 0
    visited = [False] * (N + 1)
    visited[start] = True
    dq = deque()
    for s, d in edge[start]:
        dq.append((s, d))
        visited[s] = True
    while dq:
        s, d = dq.popleft()
        if s == end:
            return d
        for e, dist in edge[s]:
            if not visited[e]:
                dq.append((e, d + dist))
                visited[e] = True
    return 0


N, M = map(int, input().split())
edge = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e, d = map(int, input().split())
    edge[s].append((e, d))
    edge[e].append((s, d))
for _ in range(M):
    s, e = map(int, input().split())
    print(bfs(s, e))


