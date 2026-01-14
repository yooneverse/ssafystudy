# from heapq import heappush, heappop
#
# def prim(start_node):
#     pq = [(0, start_node)]
#     MST = [0] * (V + 1)
#     min_weight = 0
#
#     while pq:
#         weight, node = heappop(pq)
#
#         if MST[node]:
#             continue
#
#         MST[node] = 1
#         min_weight += weight
#
#         for next_node in range(V + 1):
#             if graph[node][next_node] == 0:
#                 continue
#
#             if MST[next_node]:
#                 continue
#
#             heappush(pq, (graph[node][next_node], next_node))
#
#     return min_weight
#
# V, E = map(int, input().split())
#
# graph = [[0] * (V + 1) for _ in range(V + 1)]
#
# for _ in range(E):
#     s, e, w = map(int, input().split())
#     graph[s][e] = w
#     graph[e][w] = w
#
# result = prim(1)
#
# print(result)

import sys
sys.setrecursionlimit(10 ** 6)

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry


V, E = map(int, input().split())

result = 0
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

edges.sort(key=lambda x: x[2])
parents = [i for i in range(V + 1)]

for u, v, w in edges:
    if find_set(u) != find_set(v):
        union(u, v)
        result += w

print(result)
