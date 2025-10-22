from heapq import heappush, heappop

def dijkstra():
    global dists
    pq = [(0, N)]

    while pq:
        w, idx = heappop(pq)
        dists[idx] = min(w, dists[idx])
        if idx == K:
            return
        if idx * 2 <= 100000 and w < dists[idx * 2]:
            heappush(pq, (w, idx * 2))
        if idx - 1 >= 0 and w + 1 < dists[idx - 1]:
            heappush(pq, (w + 1, idx - 1))
        if idx + 1 <= 100000 and w + 1 < dists[idx + 1]:
            heappush(pq, (w + 1, idx + 1))

N, K = map(int, input().split())

if N > K:
    print(N - K)
else:
    inf = float('inf')
    dists = [inf] * 100001

    dijkstra()

    print(dists[K])
