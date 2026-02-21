'''
Ｎ개의 주유소
최소한 주유하여 도착하도록

도달 가능한 주유소 중 어떤 곳을 선택해야 할까
단순히 최대한 멀리 가도록 연료를 주입하는 게 아님
도착이 불가능한 경우도 존재

도착지까지 거리가 어떠냐에 따라 결과적으로 모든 주유소를 방문해야할지도

아이디어
우선순위 큐를 이용해서 필요할 때마다 주유하기

현재 도달가능한 주유소의 연료량을 큐에 넣어주어서
주유 여부를 택함

'''
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())

stations = []

for _ in range(N):
    # 주유소별 거리, 연료
    dist, gas = map(int, input().split())

    stations.append((dist, gas))

stations.sort()

# 마을까지 거리, 시작 연료
L, P = map(int, input().split())

avail_dist = P
idx = 0
pq = []
cnt = 0
# 목적지가 도달 가능 범위 내에 있다면 끝냄
# 목적지가 도달 가능 범위 밖이라면 
# 도달 가능 주유소 중 연료량 젤 큰 애를 주유하고 cnt 1 증가
# 주유소가 현재 도달 가능 범위 내에 있다면
# 주유 가능 연료를 pq에 넣어줌
while avail_dist < L:
    while idx < N and stations[idx][0] <= avail_dist:
        heappush(pq, -stations[idx][1])
        idx += 1

    if not pq:
        cnt = -1
        break
    
    nxt_gas = -heappop(pq)
    avail_dist += nxt_gas
    cnt += 1

print(cnt)
    
