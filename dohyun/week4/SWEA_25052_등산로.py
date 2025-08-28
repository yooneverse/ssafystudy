# SWEA 25052. 등산로
from collections import deque   # 덱 사용
# 길을 찾는 함수 정의
def find_way(row, col): # 행, 열 인자로 사용
    global max_len

    dist = 1    # 이동거리 변수 할당
    # 덱으로 행, 열 값 추가
    q = deque([(row, col)])
    x, y = row, col

    # 덱에 원소가 남아 있으면 반복
    # 선입선출
    while q:
        r, c = q.popleft()
        # 높이가 가장 낮은 값을 찾기 위한 변수:
        # 현재 위치의 높이로 기본값 설정
        min_h = height[r][c]
        for dr, dc in d:    # 델타 사용
            nr, nc = r + dr, c + dc
            # N x N 행렬 안에서 현재 높이보다 낮은 지점이면
            # 높이가 가장 낮은 지점 갱신 후 x, y값으로 저장
            if (0 <= nr < N and 0 <= nc < N and
                height[nr][nc] < min_h):
                min_h = height[nr][nc]
                x = nr
                y = nc
        # 만약 for문에서 x, y값이 바뀌었다면
        # 덱에 저장 / 이동 거리 증가 / 최대 거리 비교
        # 만약 안 바뀌었다면 더 낮은 지점을 찾지 못한 것이니 그대로 종료
        if (r, c) != (x, y):
            q.append((x, y))
            dist += 1
            max_len = max(max_len, dist)


T = int(input())
d = (-1, 0), (1, 0), (0, -1), (0, 1)

for tc in range(1, T + 1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]
    max_len = 1

    # 전체 행렬을 탐색해본다.
    for i in range(N):
        for j in range(N):
            find_way(i, j)

    print(f'#{tc} {max_len}')
