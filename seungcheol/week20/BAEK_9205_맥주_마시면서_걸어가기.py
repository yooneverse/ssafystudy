import sys
input = sys.stdin.readline

from collections import deque

t = int(input().strip())

def bfs(row, col):
    global answer

    que = deque([(row, col)])

    
    while que:
        r, c = que.popleft()
        if abs(festa[0] - r) + abs(festa[1] - c) <= 1000:
            answer = "happy"
            break

        for i in range(n):
            if abs(convi[i][0] - r) + abs(convi[i][1] - c) > 1000:
                continue
            if visited[i]:
                continue
            visited[i] = 1
            que.append((convi[i][0], convi[i][1]))

for testcase in range(t):
    n = int(input().strip())
    # 집
    house = list(map(int, input().split()))
    # 편의점
    convi = [tuple(map(int, input().split())) for _ in range(n)]
    # 페스티벌
    festa = list(map(int, input().split()))

    answer = "sad"
    visited = [0] * n
    bfs(house[0], house[1])

    print(answer)
