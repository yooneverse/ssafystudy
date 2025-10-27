# BAEK 2636. 치즈
# BFS, 2차원 배열
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque   # 덱 사용

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
d = (1, 0), (-1, 0), (0, 1), (0, -1)    # 델타


# 외부에 노출되는 치즈 계산
def find_air():
    # 치즈 내부 공기도 치즈로 보기 위해 1로 이뤄진 2차원 배열 생성
    air = [[1] * m for _ in range(n)]
    # 최외각 값은 전부 0이므로 초기값 0으로 설정
    air[0][0] = 0
    q = deque([(0, 0)])     # 덱 생성

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            # 배열 밖이거나 공기가 들어갈 틈이 없거나 이미 공기라면 넘어감
            if ny < 0 or ny >= n or nx < 0 or nx >= m or grid[ny][nx] or air[ny][nx] != 1:
                continue
            air[ny][nx] = 0
            q.append((ny, nx))
    melting_cheeses(air)    # 치즈 녹이기 함수 실행


# 외곽 찾기
def melting_cheeses(matrix):    # 인자로 2차원 배열 받음(외각 공기층)
    visited = [[0] * m for _ in range(n)]
    q = deque([(0, 0)])

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            # 배열 밖이거나 방문한 적 있다면 넘어감
            if ny < 0 or ny >= n or nx < 0 or nx >= m or visited[ny][nx]:
                continue
            visited[ny][nx] = 1
            # 만약 공기층과 맞닿는 치즈라면 입력된 2차원 배열에서 0으로 수정
            if matrix[ny][nx]:
                grid[ny][nx] = 0
                continue
            q.append((ny, nx))


# 초기 치즈 갯수
cheese = 0
for arr in grid:
    cheese += sum(arr)

# 반복 횟수
cnt = 0

# 치즈가 없어질 때까지 공기 노출
while True:
    ans = 0     # 남은 치즈 갯수 변수
    find_air()  # 치즈 공기 노출 함수 실행
    cnt += 1    # 반복 횟수 추가
    # 남은 치즈 갯수 계산
    for arr in grid:
        ans += sum(arr)
    # 남은 치즈가 없으면 반복 횟수와 이전에 남았던 치즈 갯수 출력
    if ans == 0:
        print(cnt)
        print(cheese)
        break
    # 남은 치즈 갯수 저장
    cheese = ans
