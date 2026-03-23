from collections import deque

board = [list(map(int, input().split())) for _ in range(5)]
sr, sc = map(int, input().split())

def idx(r, c):
    return r * 5 + c

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 시작 칸이 사과면 시작하자마자 먹은 것으로 처리
start_apple = 1 if board[sr][sc] == 1 else 0
start_mask = 1 << idx(sr, sc)

q = deque()
q.append((sr, sc, start_mask, start_apple, 0))

# 같은 위치라도 방문한 칸 집합(mask)과 먹은 사과 수가 다르면 다른 상태
visited = set()
visited.add((sr, sc, start_mask, start_apple))

answer = -1

while q:
    r, c, mask, apple, dist = q.popleft()

    if apple >= 3:
        answer = dist
        break

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        # 범위 밖
        if not (0 <= nr < 5 and 0 <= nc < 5):
            continue

        # 원래 장애물
        if board[nr][nc] == -1:
            continue

        nbit = 1 << idx(nr, nc)

        # 이미 지나간 칸이면 다시 갈 수 없음
        if mask & nbit:
            continue

        napple = apple + 1 if board[nr][nc] == 1 else apple
        nmask = mask | nbit
        state = (nr, nc, nmask, napple)

        if state in visited:
            continue

        visited.add(state)
        q.append((nr, nc, nmask, napple, dist + 1))

print(answer)