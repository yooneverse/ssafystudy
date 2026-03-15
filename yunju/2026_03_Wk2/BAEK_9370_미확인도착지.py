'''
s 지점에서 출발
최단거리로 목적지
g와 h 교차로 사이에 있는 도로 지나갔음

테케별 가능한 목적지들 오름차순으로 출력
'''
'''
g와 h를 잇는 도로를 지나갔음
해당 도로를 지나는 게 최단 거리가 되는 경우가 출력

목적지 후보들 중 타경로가 최소이면 정답이 아님
'''
'''
예시 입력
6 9 2  6개 노드, 9개 도로, 2개 목적지후보
2 3 1  2에서 출발 3과 1 잇는 도로를 지나감
1 2 1  1과 2 사이에 길이 1 도로 존재
1 3 3
2 4 4
2 5 5
3 4 3
3 6 2
4 5 4
4 6 3
5 6 7
5  목적지 후보 
6
'''
'''
출발지로부터 각 지점까지의 거리 >> 다익스트라
distance로 거리 관리 [출발지로부터 거리,]
adj로 인접 구역 관리 [[(인접노드, 거리),(인접노드,거리)],[()]]

g,h 를 지났는지 어떻게 체크할 것인가
출발지에서 g까지 최단 거리 + h에서 목적지까지 최단 거리 + gh
출발지에서 h까지 최단 거리 + g에서 목적지까지 최단 거리 + gh
1)둘 중에 짧은 것
2)출발지에서 목적지까지 최단 거리 
1)과2)가 같다면 정답
'''
'''
1차 시도 : 메모리 초과
메모리 사용량 분석
- 가장 큰 비중은 adj 리스트
- 개선 가능한 부분 pq, hpq, gpq 
distance 배열 업데이트 시점을 힙에 넣는 순간으로 변경하여 
힙을 더 줄이기 
'''
'''
2차 시도: 틀렸습니다
distance 업데이트 시점을 변경하면서 시작 노드까지 거리가 0임을 누락
while 문 밖에서 시작점 거리 0으로 설정 개선
'''
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

INF = 10**10
T = int(input())
for tc in range(T):
    # 교차로, 도로, 목적지 후보 개수
    n,m,t = map(int, input().split())
    
    # 출발지로부터 최단 거리
    distance = [INF] * (n+1)
    
    # 예술가 출발지, 지나는 교차로
    s,g,h = map(int, input().split())

    # g로부터 최단 거리
    g_distance = [INF] * (n+1)
    # h로부터 최단 거리
    h_distance = [INF] * (n+1)
    
    # 인접 노드 
    # adj[node] = [(인접노드, 거리), (인접노드, 거리),]
    adj = [[] for _ in range(n+1)]
    
    for _ in range(m):
        # a와b 사이에 d길이 양방향 도로
        a,b,d = map(int, input().split())
        adj[a].append((b,d))
        adj[b].append((a,d))

    # (현재까지 거리, 현재 노드)
    pq = [(0,s)]

    distance[s] = 0
    while pq:
        now_dist, now_node = heappop(pq)
        # 현재 노드까지 최단이 아니라면 더 이상 탐색하지 않음
        if distance[now_node] < now_dist:
            continue

        for nxt_node, nxt_dist in adj[now_node]:
            new_dist = now_dist + nxt_dist
            if distance[nxt_node] > new_dist:
                distance[nxt_node] = new_dist
                heappush(pq, (new_dist, nxt_node))

    g_distance[g] = 0
    gpq = [(0,g)]
    while gpq:
        now_dist, now_node = heappop(gpq)
        if g_distance[now_node] < now_dist:
            continue
            
        for nxt_node, nxt_dist in adj[now_node]:
            new_dist = now_dist + nxt_dist
            if g_distance[nxt_node] > new_dist:
                g_distance[nxt_node] = new_dist
                heappush(gpq, (new_dist, nxt_node))

    h_distance[h] = 0
    hpq = [(0,h)]
    while hpq:
        now_dist, now_node = heappop(hpq)
        if h_distance[now_node] < now_dist:
            continue

        for nxt_node, nxt_dist in adj[now_node]:
            new_dist = now_dist + nxt_dist
            if h_distance[nxt_node] > new_dist:
                h_distance[nxt_node] = new_dist
                heappush(hpq, (new_dist, nxt_node))    

    ans = []
    # 목적지 후보
    for _ in range(t):
        x = int(input())

        # 출발지 g h 목적지
        gh_dist = g_distance[s] + g_distance[h] + h_distance[x]
        # 출발지 h g 목적지
        hg_dist = h_distance[s] + h_distance[g] + g_distance[x]
        
        if min(gh_dist, hg_dist) == distance[x]:
            ans.append(x)
            
    ans.sort()
    print(*ans)