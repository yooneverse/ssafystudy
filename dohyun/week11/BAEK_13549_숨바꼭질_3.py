# BAEK 13549. 숨바꼭질 3
# 0-1 BFS 문제
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
# 최대 위치 제한
MAX = 100000
# 최단시간 기록을 위한 dist 배열
dist = [-1] * (MAX + 1)


def BFS():
    q = deque()
    q.append(N)
    # 초기 설정
    dist[N] = 0
    while q:
        x = q.popleft()
        # 종료 조건
        # 현재 좌표까지의 최단 시간 반환
        if x == K:
            return dist[x]

        # 2배 계산은 0초가 걸리므로 비용이 0
        # 비용이 없어 먼저 계산하기 위해 appendleft 사용
        nx = x * 2
        # 범위 내 / 방문한 적 없음 / 이전 방문 시간이 더 클 때
        if 0 <= nx <= MAX and (dist[nx] == -1 or dist[nx] > dist[x]):
            dist[nx] = dist[x]  # 그대로 치환
            q.appendleft(nx)

        for nx in (x - 1, x + 1):
            if 0 <= nx <= MAX and (dist[nx] == -1 or dist[nx] > dist[x]):
                dist[nx] = dist[x] + 1  # 1 더해서 치환
                q.append(nx)

    return -1


N, K = map(int, input().split())
print(BFS())
