import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def is_connected(nodes, adj, n):
    if not nodes:
        return False

    start_node = nodes[0]
    queue = deque([start_node])
    visited = {start_node}

    while queue:
        curr = queue.popleft()
        for neighbor in adj[curr]:

            # 인접한 노드가 현재 검사 대상 그룹(nodes)에 속해 있고, 아직 방문 전이라면
            if neighbor in nodes and neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

    # 방문한 노드의 수가 그룹의 전체 노드 수와 같다면 모두 연결된 것임
    return len(visited) == len(nodes)

def solve():

    N = int(input())

    populations = [0] + list(map(int, input().split()))

    adj = [[] for _ in range(N + 1)]

    for i in range(1, N + 1):
        data = list(map(int, input().split()))
        if data[0] > 0:
            adj[i] = data[1:]

    min_diff = float('inf')
    
    for i in range(1, (1 << N) // 2):  
        
        group_a = []

        group_b = []


        for j in range(N):
            # i의 j번째 비트가 1이면 group_a, 0이면 group_b
            if i & (1 << j):
                group_a.append(j + 1)

            else:
                group_b.append(j + 1)

        if is_connected(group_a, adj, N) and is_connected(group_b, adj, N):
            # 두 그룹 모두 연결되어 있다면 인구 차이 계산

            sum_a = sum(populations[node] for node in group_a)
            sum_b = sum(populations[node] for node in group_b)
            min_diff = min(min_diff, abs(sum_a - sum_b))


    if min_diff == float('inf'):
        print(-1)

    else:
        print(min_diff)

solve()
