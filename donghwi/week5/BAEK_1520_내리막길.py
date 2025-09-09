# https://www.acmicpc.net/problem/1520
"""
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
"""
# 재귀를 통해 시작 지점에서 목표 지점까지 이동 하며
# 탐색한 각 칸마다 갈 수 있는 길의 가지 수를 세어
# 바로 이전에 갔던 칸에 추가 한다.
import sys
# 최대 재귀 가능 횟수 늘리기
sys.setrecursionlimit(10 ** 6)


def DFS(y, x):
    # 목표 지점에 도착 했으면
    if (y, x) == (N - 1, M - 1):
        # 1로 지정후 1반환
        dp[y][x] = 1
        return 1

    # 이미 방문한 지역 이면
    if dp[y][x] != -1:
        # 그 지역 에서 갈 수 있는 경우의 수 반환
        return dp[y][x]

    # 델타
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    center = matrix[y][x]

    # 갈 수 있는 길 초기화
    way = 0

    for d in range(4):
        nr = y + dr[d]
        nc = x + dc[d]
        # 탐색한 곳이 현재 위치 에서 갈 수 있는 곳이면
        if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] < center:
            # 재귀
            way += DFS(nr, nc)

    dp[y][x] = way
    return dp[y][x]


N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
# 경우의 수
dp = [[-1] * M for _ in range(N)]

print(DFS(0, 0))

# 최종 결과 확인용
# for i in range(N):
#     print(dp[i])