'''
BAEK_2458_키 순서
큰 애 수 + 작은 애 수 == N-1 이면
→ i는 자기 빼고 나머지 모든 애들과 비교 관계가 확정된 거라서
i의 키 순서를 정확히 알 수 있음
'''
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

# graph[a] : a보다 큰 학생들 목록
graph = [[] for _ in range(N + 1)]

# rgraph[b] : b보다 작은 학생들 목록
rgraph = [[] for _ in range(N + 1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    rgraph[b].append(a)

def bfs(start, g):
    visited = [0] * (N+1)
    q = deque()

    visited[start] = 1
    q.append(start)

    cnt = 0

    while q:
        now = q.popleft()
        for nxt in g[now]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                q.append(nxt)
                cnt += 1

    return cnt

answer = 0

for i in range(1, N+1):
    taller = bfs(i, graph)
    shorter = bfs(i, rgraph)
    
    if taller + shorter == N - 1:
        answer += 1

print(answer)