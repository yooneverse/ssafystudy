T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())  # v = 노드 개수, e = 간선 개수
    adj_list = [[] for _ in range(v + 1)]

    # 인접 리스트 만들기
    for _ in range(e):
        start, end = map(int, input().split())
        adj_list[start].append(end)
        adj_list[end].append(start)

    s, g = map(int, input().split())  # s = 출발 노드, g = 도착 노드
    queue = []
    visited = [0] * (v + 1)

    queue.append(s)  # 출발점 넣고
    visited[s] = 1  # 출발점 방문했음
    while queue:
        now = queue.pop(0)

        for node in adj_list[now]:
            if not visited[node]:
                queue.append(node)
                visited[node] = visited[now] + 1

        if now == g:
            break

    if not visited[g]:
        print(f'#{test_case} {visited[g]}')
    else:
        print(f'#{test_case} {visited[g] - 1}')