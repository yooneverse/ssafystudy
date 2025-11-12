# BAEK 1240. 노드사이의 거리
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int,input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    s, e, d = map(int, input().split())
    adj[s].append((e, d))
    adj[e].append((s, d))

for _ in range(M):
    i, j = map(int, input().split())
    visited = [0] * (N + 1)
    q = deque()
    q.extend(adj[i])

    while q:
        x, dist = q.popleft()
        if x == j:
            print(dist)
            break
        for e, d in adj[x]:
            if visited[e]:
                continue
            visited[e] = 1
            q.append((e, d + dist))
