# BAEK 16235. 나무 재테크
from collections import deque
import sys
input = sys.stdin.readline

# 봄: 자신의 나이만큼 양분 흡수, 나이 + 1
# 어린 나무부터 양분을 흡수
# 양분이 부족하면 사망

# 여름: 봄에 죽은 나무의 나이 // 2 만큼 양분 추가
# 소수점 아래는 버림

# 가을: 나이가 5의 배수인 나무가 인접한 8개 칸에 번식하여 나이가 1인 나무 생성
# 땅을 벗어나지 않음

# 겨울: 땅에 양분을 A[r][c] 만큼 추가

# K년이 지난 후 살아있는 나무 개수 구하기

N, M, K = map(int, input().split())
A = []
for _ in range(N):
    A.extend([list(map(int, input().split()))])

# 최초 양분
grid = [[5] * N for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x - 1][y - 1].append(age)

d = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)

for _ in range(K):
    for i in range(N):
        for j in range(N):
            alive = deque()
            dead = 0
            for age in trees[i][j]:
                # 봄에 충분한 양분이 없으면 다음으로
                # 여름에는 죽은 나무의 나이를 2로 나눈 몫을 양분으로 추가
                if grid[i][j] < age:
                    dead += age // 2
                    continue
                grid[i][j] -= age
                alive.append(age + 1)
            trees[i][j] = alive
            grid[i][j] += dead

    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                # 가을에는 나무가 번식
                if age % 5 == 0:
                    for di, dj in d:
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= N or nj < 0 or nj >= N:
                            continue
                        # 새로 태어나는 나무를 앞으로 추가
                        trees[ni][nj].appendleft(1)

    # 겨울에는 양분 추가
    for i in range(N):
        for j in range(N):
            grid[i][j] += A[i][j]

total = sum(len(trees[i][j]) for i in range(N) for j in range(N))
print(total)
