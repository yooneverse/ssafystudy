# BAEK 15591. MooTube (Silver)
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# N: 동영상 개수
# USADO: 두 동영상이 서로 얼마나 가까운 지를 측정하는 단위
# 동영상들을 네트워크 구조로 바꿔서, 각 동영상을 정점으로 나타냄
# N-1개의 동영상 쌍을 골라서 어떤 동영상에서 다른 동영상으로 가는 경로가 반드시 하나 존재하도록 함
# == 트리
# 임의의 두 쌍 사이의 동영상의 USADO는 그 경로의 모든 연결들의 USADO 중 최솟값
# 값 K를 정해서 그 동영상과 USADO가 K 이상인 모든 동영상이 추천

N, Q = map(int, input().split())
# 인접 리스트 생성
adj_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, input().split())
    adj_list[p].append((q, r))
    adj_list[q].append((p, r))


def mootube(k, v):
    recommend_cnt = 0
    playlist = deque()
    for t in adj_list[v]:
        playlist.append(t)
    visited = [False] * (N+1)
    visited[v] = True

    while playlist:
        next, usado = playlist.popleft()
        if usado >= k:
            recommend_cnt += 1
            visited[next] = True
            for nxt, u in adj_list[next]:
                if not visited[nxt] and u >= k:
                    playlist.append((nxt, u))
    return recommend_cnt


for _ in range(Q):
    k, v = map(int, input().split())
    print(mootube(k, v))
