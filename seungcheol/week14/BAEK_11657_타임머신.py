import sys
input = sys.stdin.readline

def bellman():
    for t in range(N):
        for i in range(1, N + 1):
            for end, dist in edges[i]:
                if dists[i] != INF and dists[end] > dists[i] + dist:
                    dists[end] = dists[i] + dist
                    if t == N - 1:
                        return True
    return False

def solve():
    global N, M, edges, dists, INF

    N, M = map(int, input().split())
    edges = [[] for _ in range(N + 1)]
    INF = float('inf')
    dists = [INF] * (N + 1)
    dists[1] = 0
    for _ in range(M):
        A, B, C = map(int, input().split())
        edges[A].append((B, C))

    if bellman():
        print(-1)
    else:
        for dist in dists[2:]:
            if dist == INF:
                print(-1)
            else:
                print(dist)

solve()
