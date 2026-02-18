from collections import deque
N = int(input())


graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    # 오랜만에 하는 이 느낌
    # 양방향이라서 이렇게 해야한다.
    graph[a].append(b)
    graph[b].append(a)

# parents[i]는 i번 노드의 부모 번호를 저장
parents = [0] * (N + 1)


# 오랜만에 하니까 다까먹음 여기서 좀 제미나이 도움 완전히 받음
def bfs():
    queue = deque([1])  # 루트인 1번부터 시작

    while queue:
        current_node = queue.popleft()

        # 현재 노드와 연결된 모든 노드를 확인
        for next_node in graph[current_node]:
            # 부모가 아직 정해지지 않은 노드라면 (방문 안 한 곳이라면)
            if parents[next_node] == 0:
                parents[next_node] = current_node  # 현재 노드가 부모가 됨
                queue.append(next_node)  # 다음 탐색을 위해 큐에 넣음


bfs()

for i in range(2, N + 1):
    print(parents[i])