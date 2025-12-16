'''
문제 설명

n개의 도시 / m개의 도로
1번 도시에서 i번 도시로 가능 경로들 중 k번째 최단 경로의 소요 시간 찾기

입력
도시 개수 n / 도로 개수 m / 최단 경로 번째 수 k
(아래 m개의 줄)
도시 a / 도시 b / a->b 소요 시간 c

출력
1번 도시에서 각 도시 별로 k번째 최단 경로 소요 시간
1번 > 1번 k번째 소요 시간
1번 > 2번 k번째 소요 시간
1번 > 3번 k번째 소요 시간
...
최단 경로 없을 시 -1 출력

주의점
예시)
1번에서 1번 도시로 가는 최단 경로 소요 시간은 당연히 0임
그러나 3번째 최단 경로 소요 시간을 구하라고 한다면,
경우에 따라 경로가 없을 수 있음.
그럴 때는 -1을 출력

위 문제에서는 같은 정점이 여러 번 포함되는 것을 허용하기 때문에 왔다갔다 가능
'''

'''
아이디어

문제의 특이점
1. K번째 최단경로를 어떻게 구할 것인가
- 

두 개의 힙큐 사용
q: (현재까지 소요 시간, 현재 위치) 
distance[위치]: 해당 위치까지 소요시간들 모음 (총 K개가 모이게 됨)
'''

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]    # 인접 도시 담을 곳 (도시, 소요 시간)
for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

distance = [[] for _ in range(N+1)]

def k_shortest(start):
    q = []
    heappush(q, (0, start))      # (소요 시간, 현재 도시) 계속 다음 도시로 이동할 거임
    heappush(distance[start], 0) # start에서 start 까지 소요 시간인 0을 넣어주며 시작

    while q:
        dist, now = heappop(q)
        for nxt, w in graph[now]:
            cost = dist + w

            if len(distance[nxt]) < K:  # 아직 소요 시간이 K가지보다 적다면 계속
                heappush(distance[nxt], -cost)  # K개 소요 시간 중 K번째가 나와야 하므로 -붙임
                heappush(q, (cost,nxt))   # 현재까지 소요 시간, 해당 도시

            else:   # K가지 소요시간 아는 상태
                if (-distance[nxt][0]) > cost:    # 현재 K번째 소요 시간이 내가 새로 알게된 시간보다 오래 걸린다?
                    heappop(distance[nxt])        # K번째 소요 시간 교체
                    heappush(distance[nxt], -cost)
                    heappush(q, (cost, nxt)) # q에 추가하여 계속

# 항상 시작점은 1번 도시
k_shortest(1)
for i in range(1, N+1):
    if len(distance[i]) < K:
        print(-1)
    else:
        print(-heappop(distance[i]))