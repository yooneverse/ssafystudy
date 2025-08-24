# 10966. 물놀이를 가자
from collections import deque


def bfs():  # BFS 함수 정의
    # 방문했던 곳 저장할 행렬 생성
    # -1을 기준으로 방문 여부를 판단하고, 숫자를 증가시키면서 이동거리 계산
    visited = [[-1] * M for _ in range(N)]
    # 덱에 원소가 있으면 반복
    # 첫 번째 원소 꺼내서 사용
    # 꺼낼 때마다 이동거리 계산
    while q:
        x, y = q.popleft()
        visited[x][y] += 1
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):  # 델타 사용
            nx, ny = x + dx, y + dy
            # 방문한 적 없고, 지도 행렬 상 물이 아니면 덱에 저장
            # 방문할 예정이므로 지금까지 이동한 거리를 저장해서 다음 계산에 사용
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and str_map[nx][ny] != 'W':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y]
    # 덱에 원소가 없으면 방문할 수 있는 모든 곳 가본 것임
    # 이동거리를 방문 행렬에 저장했으므로 반환
    return visited


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    str_map = [input() for _ in range(N)]
    result = 0
    q = deque()  # 덱 사용
    # 물이 있는 곳을 미리 모아서 덱에 저장한다
    # 왜냐하면 BFS는 '선입선출'이므로 최소 이동거리를 구하기 위해서는
    # 물이 있는 곳 근처의 갈 수 있는 지점을 미리 구해서
    # 이동거리를 계산해둬야 하기 때문
    for i in range(N):
        for j in range(M):
            if str_map[i][j] == 'W':
                q.append((i, j))
    # 출력 방식:
    # 1) BFS 함수에서 반환된 이동거리 행렬을 행끼리 더한다
    # => map(sum, bfs())
    # 2) 행끼리 더한 값을 sum()으로 묶어줘서 모든 값을 더한다.
    # 이것이 가능한 이유는 W 지점은 0이고, L 지점은 최소 이동거리로 나타나기 때문
    print(f'#{tc} {sum(map(sum, bfs()))}')
