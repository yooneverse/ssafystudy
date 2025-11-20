# TODO: 도달가능:HaruHaru 도달불가:Hing
# (0,0)에서 출발해서 제일 끝 (N-1,N-1)에 도달
# 오른쪽, 아래만 이동 가능

from collections import deque

def jumpjelly(r,c):
    q = deque()
    visited = [[0] * N for _ in range(N)]
    q.append((r,c))
    visited[r][c] = 1

    while q:
        sr, sc = q.popleft()
        # 얼만큼 뛸건지 저장
        jump = board[sr][sc]

        # 목적지에 도달했다면
        if sr == N-1 and sc == N-1:
            print('HaruHaru')
            return

        # 오른쪽, 아래 두 방향만 이동
        for nr, nc in [(sr, sc + jump), (sr + jump, sc)]:
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))

    # 도달 불가시
    print("Hing")

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

jumpjelly(0,0)