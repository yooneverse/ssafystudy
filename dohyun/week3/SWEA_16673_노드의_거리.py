# 16673. 6일차 - 노드의 거리
from collections import deque


# 최소 간선 갯수를 찾는 함수 정의
# 출발 노드와 도착 노드를 인자로 받음
# 출발 노드를 덱에 저장
def find_path():
    q.append(S)
    # 덱에 원소가 남아있으면 반복
    # 맨 앞의 원소를 꺼내서 사용
    while q:
        t = q.popleft()
        # 만약 현재 노드와 도착 노드가 같다면 이동거리 반환 
        if t == G:
            return visited[G]
        # 인접 배열에서 노드 값을 순회
        # 만약 그 노드에 방문하지 않았다면 덱에 저장
        # 방문 예정 기록하며 이동거리 계산
        for w in adj_l[t]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[t] + 1
    # G까지 간선으로 연결되지 않았으면 0 반환
    return 0
            


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 입력받은 간선 정보가 일렬로 배치되도록 .extend 사용해 행렬 생성
    line = []
    for i in range(E):
        line.extend(map(int, input().split()))
    # 출발 노드와 도착 노드 입력
    # 방문했던 기록 행렬로 이동거리 계산할 예정
    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    q = deque() # 덱 사용
    # 1부터 노드 개수 + 1까지 인접 배열 생성
    # 노드 번호에 따라서 인접한 노드 번호 저장
    # 화살표가 없으므로 왕복 통행 가능하도록 설정
    adj_l = [[] for _ in range(V + 1)]
    for i in range(E):
        v1, v2 = line[i * 2], line[i * 2 + 1]
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)
    # 함수 호출 후 출력
    print(f'#{tc} {find_path()}')
