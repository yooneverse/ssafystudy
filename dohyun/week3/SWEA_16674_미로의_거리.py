# 16674. 6일차 - 미로의 거리
from collections import deque


# 미로 탈출 함수 정의
def find_move():
    # 미로 행렬에서 값이 2인 시작점 찾고
    # 덱에 저장
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                q.append((i, j))
                break
        # 이중 for 문 탈출용
        if q:
            break
    # 덱에 원소가 남아있으면 반복
    # 맨 앞의 원소를 꺼내서 사용
    while q:
        r, c = q.popleft()
        # if not visited[r][c]:
        #     visited[r][c] = True
        for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1): # 델타 사용
            nr, nc = r + dr, c + dc
            # 만약 방문한 적이 없고
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                # 미로 행렬에서 값이 0이면 덱에 저장
                # 방문했다고 기록하면서 이동거리 증가
                if maze[nr][nc] == '0':
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
                # 다음 방문할 곳의 미로 행렬 값이 3이면 이동했던 값 반환
                elif maze[nr][nc] == '3':
                    return visited[r][c]
    # 도착점까지 경로를 못 찾으면 0 반환
    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 미로 행렬 생성
    maze = [input() for _ in range(N)]
    q = deque() # 덱 사용
    # 방문했던 곳 기록하며 이동거리 계산할 행렬 생성
    visited = [[0] * N for _ in range(N)]

    print(f'#{tc} {find_move()}')
