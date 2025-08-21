from collections import deque

def maze_runner(s, g):
    # visited 만들기
    visited = [0] * (V+1)
    # print(visited) [0, 0, 0, 0, 0, 0, 0]
    # q 만들기
    q = deque()
    # q에 시작정점 추가하기
    q.append(s)
    # 추가하면서 visited 방문했다고 하기
    visited[s] = 1

    # 이제 시작정점을 시작으로 q가 빌때까지 움직일거임
    while q:
        # 추가했던 시작정점 s를 다시 꺼냄
        v = q.popleft()
        # 만약 꺼낸 원소가 g면, 반환
        if v == g:
            # 시작점을 1로 설정했으므로 -1 해줘야 거리가 나옴
            return visited[v] - 1

        # v 원소에 인접한 원소들 중
        for nv in graph[v]:
            # 방문 안한 애가 있다면
            if visited[nv] == 0:
                # 다음에 방문할거라고 넣어주기
                q.append(nv)
                visited[nv] = visited[v] + 1

    # 다 돌았는데 연결 안되어 있으면 0 출력
    return 0

T = int(input())
for tc in range(1, T+1):
    # 정점, 노드
    V, E = map(int, input().split())
    # 그래프 만들어주기 (리스트)
    graph = [[] for _ in range(V+1)]

    # 정점 입력받기 (간선의 개수만큼)
    for _ in range(E):
        # 두개씩 들어오니까
        a, b = map(int, input().split())

        # 서로 이어지니까 (무방향)
        graph[a].append(b)
        graph[b].append(a)

    # 시작점, 도착점
    S, G = map(int, input().split())

    answer = maze_runner(S, G)
    print(f'#{tc} {answer}')