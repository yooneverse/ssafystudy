# 내리막길
# 옛날에 풀었던 문제네요

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def my_map(sr,sc):
    # 만약 도착점에 도달하면
    if sr == N -1 and sc == M -1:
        return 1

    # 만약 이쪽길로 가본적이 있다면
    if dp[sr][sc] != -1:
        return dp[sr][sc]

    # 이 칸에서부터 출발!
    dp[sr][sc] = 0
    for k in range(4):
        nr = sr + dr[k]
        nc = sc + dc[k]
        if 0<=nr<N and 0<=nc<M and matrix[nr][nc] < matrix[sr][sc]:
            dp[sr][sc] += my_map(nr,nc)

    return dp[sr][sc]


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 구하고 싶은 값 : 내리막길로 가는 경로의 수
# dp배열
dp = [[-1] * M for _ in range(N)]

# 함수 호출 (출발지점은 언제나 0,0
print(my_map(0,0))