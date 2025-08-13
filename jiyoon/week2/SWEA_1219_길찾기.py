T = 10  # 고정된 테스트케이스 수

for tc in range(1, T + 1):
    # 번호랑 간선 수 받기 (번호는 안 쓰고 E만 쓸 것)
    tc_num, E = map(int, input().split())

    # 간선 정보가 2*E개 될 때까지 입력 받기
    data = []
    while len(data) < 2 * E:
        data.extend(map(int, input().split()))

    # 정점 개수, 인접리스트 만들기
    V = 100
    adj = [[] for _ in range(V)]
    for i in range(0, 2 * E, 2):
        s, e = data[i], data[i + 1]
        adj[s].append(e)

    # 시작점, 도착점, 방문 기록, 스택, 정답 기본값
    S, G = 0, 99
    visited = [0] * V
    stack = [S]
    answer = 0

    # DFS 반복문 (스택 사용)
    while stack:
        # 스택에서 하나 꺼내기
        v = stack.pop()

        # 이미 방문한 곳이면 건너뛰기
        if visited[v]:
            continue

        # 방문 표시
        visited[v] = 1

        # 도착점이면 성공 처리하고 종료
        if v == G:
            answer = 1
            break

        # 현재 정점에서 갈 수 있는 곳을 스택에 추가
        for nv in adj[v]:
            if not visited[nv]:
                stack.append(nv)

    # 결과 출력
    print(f"#{tc} {answer}")
