from heapq import heappush, heappop

def prim(n, cnt):
    pq = edges[n][:]
    visited[n] = 1
    weight = 0
    while pq and cnt < V:
        dist, end = heappop(pq)

        if visited[end]:
            continue

        weight += dist
        visited[end] = 1
        cnt += 1

        for nxt_dist, nxt in edges[end]:
            if visited[nxt]:
                continue
            heappush(pq, (nxt_dist, nxt))
    return weight


def kruskal():
    n = weight = 0
    while k_edges and n < V - 1:
        dist, start, end = heappop(k_edges)

        if union(start, end):
            continue

        weight += dist
        n += 1

    return weight


def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    # 이미 같은 집합이면 True 반환하고 종료
    if rep_x == rep_y:
        return True

    # 다른 집합이면 rank에 따라서 다른 집합을 아래로 넣고 False 반환하고 종료
    if rank[rep_x] == rank[rep_y]:
        rank[rep_x] += 1
        parent[rep_y] = rep_x
    elif rank[rep_x] > rank[rep_y]:
        parent[rep_y] = rep_x
    else:
        parent[rep_x] = rep_y
    return False


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


V, E = map(int, input().split())

edges = [[] for _ in range(V + 1)]
k_edges = []
for i in range(E):
    s, e, d = map(int, input().split())
    # prim 사용
    heappush(edges[s], (d, e))
    heappush(edges[e], (d, s))

    # kruskal 사용
    heappush(k_edges, (d, s, e))

# prim
visited = [0] * (V + 1)

prim_answer = prim(1, 0)

print(prim_answer)

# kruskal
parent = [i for i in range(V + 1)]
rank = [0] * (V + 1)

kruskal_answer = kruskal()

print(kruskal_answer)
