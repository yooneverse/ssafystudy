from collections import deque

def bfs(N, people, a, b):
    dist = [-1] * (N+1)

    q = deque()
    
    dist[a] = 0
    q.append(a)

    while len(q) > 0:
        now = q.popleft()

        if now == b:
            return dist[now]
        
        for nxt in people[now]:
            # 아직 방문 안 한 사람만 방문
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)

    return -1

# 총 사람의 수
N = int(input())
# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
a, b = map(int, input().split())
# 부모 자식들 간의 관계의 개수
M = int(input())

people = [[] for _ in range(N+1)]

# 부모 자식간의 관계를 나타내는 두 번호
for _ in range(M):
    x, y = map(int, input().split())
    people[x].append(y)
    people[y].append(x)

print(bfs(N, people, a, b))