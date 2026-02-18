import sys
input = sys.stdin.readline

# 1. 노드 개수 입력
n = int(input())

# 2. 인접 리스트 생성 (1번부터 n번까지 사용)
graph = [[] for _ in range(n + 1)]

# 3. 간선 입력 (트리는 간선이 n-1개)
for _ in range(n - 1):
    a, b = map(int, input().split())
    
    # 무방향 그래프이므로 양쪽 모두 추가
    graph[a].append(b)
    graph[b].append(a)

# 4. 부모 정보를 저장할 배열
#    parent[i] = i번 노드의 부모
#    0이면 아직 방문하지 않은 상태
parent = [0] * (n + 1)

# 5. 루트 노드(1번) 방문 처리
parent[1] = -1  # 루트는 부모 없음 (출력하지 않음)

# 6. DFS를 위한 스택 초기화
stack = [1]

# 7. 반복 DFS 수행
while stack:
    current = stack.pop()
    
    # 현재 노드와 연결된 노드 확인
    for next_node in graph[current]:
        
        # 아직 방문하지 않은 경우
        if parent[next_node] == 0:
            
            # 현재 노드를 부모로 기록
            parent[next_node] = current
            
            # 다음 탐색을 위해 스택에 추가
            stack.append(next_node)

# 8. 2번 노드부터 n번 노드까지 부모 출력
print("\n".join(str(parent[i]) for i in range(2, n + 1)))
