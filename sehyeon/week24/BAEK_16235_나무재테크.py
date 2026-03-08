import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

# 현재 땅의 양분 (처음에는 5)
nut = [[5]*N for _ in range(N)]

# 각 칸의 나무들
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

# 나이 어린 순으로 정렬
for i in range(N):
    for j in range(N):
        trees[i][j] = deque(sorted(trees[i][j]))

# 8방향
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(K):

    # 봄 & 여름
    dead = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not trees[i][j]:
                continue

            survive = deque()
            dead = 0

            for age in trees[i][j]:

                # 양분 먹을 수 있음
                if nut[i][j] >= age:
                    nut[i][j] -= age
                    survive.append(age + 1)

                # 양분 부족 => 죽어
                else:
                    dead += age // 2

            nut[i][j] += dead
            trees[i][j] = survive


    # 가을 
    add = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if age % 5 == 0:
                    for d in range(8):
                        nx, ny = i + dx[d], j + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny].appendleft(1)

    # 겨울 
    for i in range(N):
        for j in range(N):
            nut[i][j] += A[i][j]


# 살아있는 나무 수
result = 0
for i in range(N):
    for j in range(N):
        result += len(trees[i][j])

print(result)
                                            