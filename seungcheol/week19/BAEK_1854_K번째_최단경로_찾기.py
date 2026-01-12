import sys
input = sys.stdin.readline

from heapq import heappop, heappush

def input_data():
    N, M, K = map(int, input().split())

    edges = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))
    return N, M, K, edges

def dijkstra():
    answer = [[] for _ in range(N + 1)]
    heappush(answer[1], 0)

    start = [(0, 1)]
    while start:
        dist, prev = heappop(start)

        for nxt, nxt_dist in edges[prev]:
            new_dist = dist + nxt_dist

            if len(answer[nxt]) == K:
                if -answer[nxt][0] > new_dist:
                    heappop(answer[nxt])
                    heappush(answer[nxt], -new_dist)
                    heappush(start, (new_dist, nxt))
            else:
                heappush(answer[nxt], -new_dist)
                heappush(start, (new_dist, nxt))
    return answer


N, M, K, edges = input_data()

answer = dijkstra()

for i in range(1, 1 + N):
    if len(answer[i]) < K:
        print(-1)
    else:
        print(-answer[i][0])


# import sys
# input = sys.stdin.readline
#
# from heapq import heappop, heappush
#
# def dijkstra():
#     start = [(0, 1)]
#     while start:
#         dist, prev = start.pop()
#
#         for nxt, nxt_dist in edges[prev]:
#             heappush(answer[nxt], dist + nxt_dist)
#             if len(answer[nxt]) <= K:
#                 heappush(start, (dist + nxt_dist, nxt))
#
#
# N, M, K = map(int, input().split())
#
# edges = [[] for _ in range(N + 1)]
# answer = [[] for _ in range(N + 1)]
# heappush(answer[1], 0)
#
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     edges[a].append((b, c))
#
# dijkstra()
#
# for i in range(1, 1 + N):
#     if len(answer[i]) < K:
#         print(-1)
#     else:
#         tmp = -1
#         for _ in range(K):
#             tmp = heappop(answer[i])
#         print(tmp)
