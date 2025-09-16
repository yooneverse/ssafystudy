def virus(v):
    visited[v] = 1
    for nxt in computer[v]:
        if visited[nxt] == 0:
            virus(nxt)


N = int(input())
E = int(input())
computer = [[] for _ in range(N+1)]
for _ in range(E):
    # 컴퓨터 수만큼 입력받아주기
    a, b = map(int, input().split())
    # 무방향이므로 서로 이어주기
    computer[a].append(b)
    computer[b].append(a)

visited = [0] * (N+1)
# 1번 컴퓨터부터 시작
virus(1)
print(visited.count(1)-1)