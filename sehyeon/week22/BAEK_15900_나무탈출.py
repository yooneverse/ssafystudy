# '나무 탈출' 은 N개의 정점이 있는 트리 모양으로 생긴 게임판과 몇 개의 게임말로 이루어진다
# 자식이 없는 노드는 '리프 노드' 라고 불린다.
# 성원이가 최선을 다했을 때 이 게임을 이길 수 있으면 Yes, 아니면 No를 출력한다.
# 각 리프는 하나의 “독립된 게임 가지”라고 봐야함!
# 이동횟수 = 깊이
# 전체 이동 횟수의 홀짝 싸움
# 따라서 성원이가 먼저 시작하므로 깊이 합이 홀일 때 승리함!

import sys
sys.setrecursionlimit(10**6) # 시간 초과 이슈ㅜㅜ
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

total = 0

# (현재 위치 노드, 직전에 왔던 노드, 현재까지 이동한 횟수)
def dfs(node, parent, depth):
    global total
    is_leaf = True

    for next in graph[node]:
        # 부모는 다시 돌아가면 안되므로 제외시킴
        if next != parent:
            # 자식 존재하면 리프노드 아니므로 깊이+1 -> 함수 다시 실행
            is_leaf = False
            dfs(next, node, depth + 1)
    
    # 리프노드면 이동횟수 다 더함
    if is_leaf:
        total += depth

dfs(1, 0, 0)

if total % 2 == 1:
    print("Yes")
else:
    print("No")