# BAEK 1937. 욕심쟁이 판다
import sys
sys.stdin = open('input.txt', 'r')
# Python 3 환경에서 재귀 한도 초과뜸
sys.setrecursionlimit(10000)


def panda(y, x):    # dfs 함수
    # 메모이제이션 값 존재하면 반환
    if dp[y][x]:
        return dp[y][x]
    # 없으면 1로 시작
    dp[y][x] = 1
    # 상하좌우 확인
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        # 다음 칸이 더 높으면 더 큰 값으로 메모이제이션 실행
        if matrix[y][x] < matrix[ny][nx]:
            dp[y][x] = max(dp[y][x], panda(ny, nx) + 1)
    # 메모이제이션 값 봔환
    return dp[y][x]


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
# dp 배열 생성
dp = [[0] * n for _ in range(n)]
d = (-1, 0), (1, 0), (0, -1), (0, 1)

best = 0    # 최댓값 변수
result = []
# n x n 배열 탐색
for i in range(n):
    for j in range(n):
        # 최댓값 찾기
        best = max(best, panda(i, j))

print(best)
