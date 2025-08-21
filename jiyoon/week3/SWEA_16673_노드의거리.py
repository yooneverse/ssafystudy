from collections import deque

def bfs(s, g):
    visited = [0] * (V + 1)
    q = deque()
    # 시작점 넣어놓고 시작하기
    q.append(s)
    visited[s] = 1

    while q:
        v = q.popleft()

        for nv in adj_l[v]:
            if visited[nv] == 0:  # 아직 방문 안 했다면
                q.append(nv)
                visited[nv] = visited[v] + 1

                if nv == g:       # 도착지에 도달하면 바로 종료 가능
                    return visited[g] - 1

    return 0  # while문 끝날 때까지 도착지에 도달하지 못함 = 연결되지 못함 = 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 인접 리스트 초기화
    adj_l = [[] for _ in range(V + 1)]

    # E개의 간선 입력
    for _ in range(E):
        s, g = map(int, input().split()) # E개의 줄에 거쳐 한 줄씩 주어진 데이터 받아옴
        adj_l[s].append(g) # s-g 인접
        adj_l[g].append(s) # g-s 인접

    S, G = map(int, input().split())  # 출발-도착 짝짓기

    distance = bfs(S, G)
    print(f"#{tc} {distance}")

