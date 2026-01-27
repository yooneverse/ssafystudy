# BAEK 16236. 아기 상어
import sys
from collections import deque
from heapq import heappop, heappush
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 아기 상어보다 큰 물고기가 있는 칸은 지나갈 수 없음.
# 자신의 크기보다 작은 물고기만 먹을 수 있음.
# 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
# 처음 아기 상어의 크기는 2
# 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
d = (-1, 0), (0, -1), (0, 1), (1, 0)
total_dist = 0  # 총 이동거리


# 처음 상어 위치 탐색 함수
def find_shark():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9:
                return i, j


# 먹을 수 있는 물고기 찾는 함수
def find_fish(r, c, size):
    fishes = []
    q = deque([(r, c, 0)])  # y좌표, x좌표, 거리
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    min_dist = float('inf')  # 최소 거리 변수

    while q:
        y, x, dist = q.popleft()
        # 만약 현재 이동한 거리가 최소 거리를 넘어서면 반복 중단
        if dist > min_dist:
            break

        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if visited[ny][nx]:
                continue
            # 이동하려는 곳의 물고기가 상어 크기보다 크면 이동 불가
            if grid[ny][nx] > size:
                continue
            # 이동하려는 곳의 물고기가 상어 크기보다 작으면 거리, y좌표, x좌표 힙에 추가
            # 최소 거리 갱신
            if 0 < grid[ny][nx] < size:
                heappush(fishes, (dist + 1, ny, nx))
                min_dist = dist + 1
            # 다음 이동할 곳의 y좌표, x좌표, 거리 덱에 추가
            q.append((ny, nx, dist + 1))
            visited[ny][nx] = True
    # 물고기 거리, 위치 힙 반환
    return fishes


# 물고기 먹으러 가는 함수
def feeding(r, c, size):
    global total_dist   # 총 이동거리 전역변수 설정
    feed_cnt = 0        # 먹이 먹은 횟수 변수

    while True:
        next_fish = find_fish(r, c, size)
        # 다음으로 먹을 물고기가 없다면 반복 중단
        if not next_fish:
            break
        # 거리, y좌표, x좌표 꺼내서 총 이동 거리 갱신
        dist, nr, nc = heappop(next_fish)
        total_dist += dist
        # 현재 위치 갱신
        r, c = nr, nc
        grid[nr][nc] = 0
        # 먹이 먹은 횟수 갱신 후 크기 계산
        feed_cnt += 1
        if feed_cnt == size:
            feed_cnt = 0
            size += 1


# 처음 상어 위치 탐색 후 상어 위치 빈 칸으로 만듦
r, c = find_shark()
grid[r][c] = 0
feeding(r, c, 2)    # 상어 최초 크기는 2
print(total_dist)
