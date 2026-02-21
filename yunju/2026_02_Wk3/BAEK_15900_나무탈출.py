import sys

from collections import deque

input = sys.stdin.readline

N = int(input())

adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):

    a, b = map(int, input().split())

    adj[a].append(b)

    adj[b].append(a)

visited = [-1] * (N + 1)

ans = 0

q = deque()

q.append(1)

visited[1] = 0

while q:

    now = q.popleft()

    

    is_leaf = True

    for nxt in adj[now]:

        if visited[nxt] == -1:

            visited[nxt] = visited[now] + 1

            q.append(nxt)

            is_leaf = False

            

    if is_leaf:

        ans += visited[now]

if ans % 2 == 1:

    print("Yes")

else:

    print("No")

