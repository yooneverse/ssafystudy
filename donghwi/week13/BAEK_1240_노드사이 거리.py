def dfs(start, result):
    if start == b:
        print(result)
        return

    for end, weight in graph[start]:
        if not visited[end]:
            visited[end] = True
            dfs(end, result + weight)
            visited[end] = False


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

for _ in range(M):
    a, b = map(int, input().split())
    visited = [False] * (N + 1)
    visited[a] = True
    dfs(a, 0)