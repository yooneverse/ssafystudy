#import sys
#sys.stdin = open("input.txt", "r")

NODE_NUN = 100

def DFS(s, e):
    global adj_list, node
    stack = []
    visited = [0] * (NODE_NUN + 1)
    
    # 시작점 저장
    now_node = s
    move = 0

    while now_node != e:

        
        # 인접 노드 찾기
        for adj_node in adj_list[now_node]:
            # 인접 노드가 있는데 방문을 안했다
            if visited[adj_node] == 0:
                stack.append(now_node) # 지나온 점 stack 저장
                visited[now_node] = 1 # 지나온 점 visitied 표시
                now_node = adj_node # 인접 노드로 이동
                move += 1
                break
        
        # 인접노드가 없다.
        else:
            visited[now_node] = 1
            now_node = stack.pop()
        
        # 도착지 빼고 모든 노드 다 간 상황
        if not stack:
            return 0
    return 1


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test_num, node = map(int, input().split())
    graph = list(map(int, input().split()))

    # 인접 리스트 저장
    adj_list = [[] for _ in range(NODE_NUN + 1)]
    for i in range(node):
        start = graph[i * 2]
        end = graph[i * 2 + 1]
        adj_list[start].append(end)

    print(f'#{test_num} {DFS(0,99)}')
    
