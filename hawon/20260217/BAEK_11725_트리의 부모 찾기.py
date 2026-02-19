# 트리의 부모 찾기

import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, start_node, parent):
    q = deque()
    q.append(start_node)

    parent[start_node] = -1

    while q:
        now = q.popleft()

        # now와 연결된 애들을 다 확인하기
        for nxt in graph[now]:
             
             if parent[nxt] == 0:
                parent[nxt] = now

                q.append(nxt)

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N+1)

bfs(graph, 1, parent)

for i in range(2, N + 1):
    print(parent[i])