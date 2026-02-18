import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# 깊이 저장용 배열 만들어두기
depth = [-1] * (n + 1)
depth[1] = 0  # 루트는 깊이 0

q = deque([1])

# 1번에서 시작해 모든 노드 깊이 구하기
while q:
    cur = q.popleft()
    for nxt in g[cur]:
        if depth[nxt] == -1:
            depth[nxt] = depth[cur] + 1
            q.append(nxt)

# 리프 깊이 합 계산
total = 0
for i in range(2, n + 1):        # 1번 제외
    if len(g[i]) == 1:           # 연결이 하나면 리프
        total += depth[i]

# 홀짝 판단
print("Yes" if total % 2 == 1 else "No")
