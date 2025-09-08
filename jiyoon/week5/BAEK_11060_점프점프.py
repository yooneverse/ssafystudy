# 입력 받기: N, 배열 A
from collections import deque

N = int(input())
maze = list(map(int, input().split()))

visited = [False] * (N+1)   # 방문 여부
min_jump = [-1] * (N+1)     # 최소 점프 횟수 기록

q = deque()
q.append(1)          # 시작 칸
visited[1] = True
min_jump[1] = 0      # 시작은 점프 0번

while q:
    now = q.popleft()
    if now == N:                # 끝 칸에 도착하면 출력
        print(min_jump[now])
        break
    # 현재 칸에서 점프할 수 있는 범위 확인
    for nxt in range(now+1, now+maze[now-1]+1):
        if nxt <= N and not visited[nxt]:
            visited[nxt] = True
            min_jump[nxt] = min_jump[now] + 1
            q.append(nxt)

if min_jump[N] == -1:   # 끝까지 못 갔으면 -1 출력
    print(-1)
