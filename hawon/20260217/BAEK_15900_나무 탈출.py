'''
1번 정점 - 루트 노드
자식 없음 - 리프 노드
리프 노드에 게임말들이 놓여있는 채로 시작, 부모 노드로 옮기면서 루트 노드에 도착하면 게임 말을 제거
게임말이 게임판에 존재하지 않을 때 차례면 패배
성원이가 선, 이기면 yes / 지면 no
깊이가 짝수면 지고, 홀수면 이김
'''

import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

q = deque()
# 노드번호, 깊이
q.append((1,0))
visited[1] = 1

# 리프의 depth
depth_sum = 0

while q:
    now, depth = q.popleft()
    
    is_leaf = True

    for nxt in graph[now]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            q.append((nxt, depth + 1))
            is_leaf = False

    # 자식이 하나도 없으면 리프 노드
    if is_leaf:
        depth_sum += depth

# 리프 깊이 합이 홀수면 선공 승
if depth_sum % 2 == 1:
    print("Yes")
else:
    print("No")
