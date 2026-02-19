# 윗줄 맨 왼쪽 방은 시작방으로서 항상 흰 방이고, 아랫줄 맨 오른쪽 방은 끝방으로서 역시 흰 방이다.
# 시작방에서 출발하여 길을 찾아서 끝방으로 가는 것이 목적인데,
# 부득이 검은 방 몇 개를 흰 방으로 바꾸어야 하는데 되도록 적은 수의 방의 색을 바꾸고 싶다.
# 검은 방에서 흰 방으로 바꾸어야 할 최소의 수를 구하는 프로그램을 작성하시오.
# 단, 검은 방을 하나도 흰방으로 바꾸지 않아도 되는 경우는 0이 답이다.
# 1: 흰, 0: 검
# 0-1 BFS 사용!!!

from collections import deque

n = int(input())
board = []

for i in range(n):
    row = list(map(int, input()))
    board.append(row)

INF = int(1e8)
dist = [[INF] * n for _ in range(n)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0,0))
dist[0][0] = 0  # 최소로 부순 검은방의 개수

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안이고
        if 0 <= nx < n and 0 <= ny < n:

            # 흰방이면 그대로
            if board[nx][ny] == 1:
                new_cost = dist[x][y]
            # 검은방이면 +1 (부숨)
            else:
                new_cost = dist[x][y] + 1

            # 더 적게 부순걸로 갱신
            if dist[nx][ny] > new_cost:
                dist[nx][ny] = new_cost
                
                # 흰방이면 앞에 넣어서 먼저 탐색(비용 0)
                if board[nx][ny] == 1:
                    q.appendleft((nx, ny))
                # 검은방이면 뒤에 넣어서 나중에 탐색(비용 1)
                else:
                    q.append((nx, ny))

print(dist[n-1][n-1])