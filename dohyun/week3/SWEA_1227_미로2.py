# 1227. [S/W 문제해결 기본] 7일차 - 미로2
from collections import deque   # 덱 사용


def BFS():  # BPS 함수 정의
    # 덱에 원소가 남아있으면 반복
    # 맨 앞의 원소를 꺼내서 사용
    while q:
        i, j = q.popleft()
        for di, dj in d:    # 델타 설정
            ni, nj = i + di, j + dj
            # 델타 범위로 탐색하며 방문하지 않았고
            # 행렬상 값이 1이 아니면 덱에 등록하고 방문할 예정이라고 행렬에 저장
            if (0 <= ni < N and 0 <= nj < N and
                    not visited[ni][nj] and
                    maze[ni][nj] != '1'):
                # 만약 행렬상의 값이 3이면 1 반환
                if maze[ni][nj] == '3':
                    return 1
                q.append((ni, nj))
                visited[ni][nj] = 1
    # 그외 0 반환
    return 0


T = 10

for tc in range(1, T + 1):
    t = input()
    # 미로 행렬의 크기 N
    N = 100
    # 문자열 그대로 행렬 배치
    maze = [input() for _ in range(N)]
    # 미로의 시작점 지정
    s = (1, 1)
    # 덱 생성 후 시작점 삽입
    q = deque()
    q.append(s)
    # 들렀던 곳 저장할 행열 생성 후 시작점 삽입
    visited = [[0] * N for _ in range(N)]
    visited[2][2] = 1
    d = (-1, 0), (1, 0), (0, -1), (0, 1)    # 델타 사용

    print(f'#{tc} {BFS()}')
