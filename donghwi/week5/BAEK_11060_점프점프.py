from collections import deque

N = int(input().strip())
arr = list(map(int, input().split()))

dist = [-1] * N
dist[0] = 0
q = deque([0])

while q:
    i = q.popleft()
    if i == N - 1:
        break
    for nx in range(i + 1, min(N, i + arr[i] + 1)):
        if dist[nx] == -1:
            dist[nx] = dist[i] + 1
            q.append(nx)

print(dist[N - 1])
