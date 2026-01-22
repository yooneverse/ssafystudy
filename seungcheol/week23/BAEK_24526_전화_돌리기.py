import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)

# 0 = 미방문
# 1 = 탐색 중 (스택)
# 2 = 처리 완료
state = [0] * (n + 1)

# 1 = 제거 대상 (사이클 또는 도달)
bad = [0] * (n + 1)

# 모든 노드 확인
for start in range(1, n + 1):
    # 방문한 노드면 생략
    if state[start]:
        continue

    # 방문노드, 현재 노드가 방문 가능한 다음 노드의 인덱스
    stack = [(start, 0)]

    # 현재 노드 탐색 중
    state[start] = 1

    # dfs
    while stack:
        # 현재 노드, 다음 노드 인덱스
        u, idx = stack[-1]

        # 마지막 인덱스까지 확인
        if idx < len(edges[u]):
            # 다음 노드
            v = edges[u][idx]

            # 인덱스 + 1
            stack[-1] = (u, idx + 1)

            # 다음 노드 방문한 적이 없으면
            # 노드 탐색 표시, stack에 append
            if state[v] == 0:
                state[v] = 1
                stack.append((v, 0))

            # 다음 노드가 탐색중이면
            # 사이클 생성이므로 u 사이클 처리
            # 이후 pop하게 된다면 u가 v로 취급되고
            # state[u] == 1이므로 이전 노드들도 차례대로 사이클 처리 됨
            elif state[v] == 1:
                # 사이클 발견
                bad[u] = 1

            # state[v] == 2
            else:
                # 탐색 종료된 노드가 사이클인 경우
                # 사이클에 도달가능 한 경우로 처리됨
                if bad[v]:
                    bad[u] = 1

        # 다음 노드가 없는 경우(인덱스 범위 초과인 경우도 포함)
        else:
            # stack에서 pop
            # 탐색 종료
            stack.pop()
            state[u] = 2

            # 이전 노드가 존재하고 현재 노드가 사이클이면
            # 이전 노드 사이클에 도달 가능 표시
            if stack and bad[u]:
                parent, _ = stack[-1]
                bad[parent] = 1

answer = -1
for num in bad:
    if not num:
        answer += 1

print(answer)
