import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

parent = [False] * (N+1)
parent[1] = True

q = deque()
q.append(1)

while q:
    s = q.popleft()
    for nxt in adj[s]:
        if parent[nxt] == False:
            parent[nxt] = s

            q.append(nxt)

for i in range(2,N+1):
    print(parent[i])