# stack 이용으로 재귀제한 극복한 dfs
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N = int(input())

bamboo = [list(map(int, input().split())) for _ in range(N)]

# 현재 위치에서 출발해서 가장 멀리 이동가능한 거리 저장
dp = [[0] * N for _ in range(N)]

def dfs(start_r, start_c):

    # 출발 위치, dp 확정 확인 변수
    stack = [(start_r, start_c, False)]

    while stack:
        r, c, done = stack.pop()

        # dp 확정
        if done:
            dp[r][c] = max(dp[r][c], 1)
            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                if bamboo[nr][nc] > bamboo[r][c]:
                    dp[r][c] = max(dp[r][c], dp[nr][nc] + 1)
                    continue

        # 계산된 경우 스킵
        if dp[r][c]:
            continue

        stack.append((r, c, True))

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if bamboo[nr][nc] > bamboo[r][c]:
                if not dp[nr][nc]:
                    stack.append((nr, nc, False))

for i in range(N):
    for j in range(N):
        dfs(i, j)

answer = 0
for x in range(N):
    answer = max(answer, *dp[x])

print(answer)

# gpt 풀이 - dp 1차원 배열(오름차순으로 정렬)
# import sys
# input = sys.stdin.readline
#
# delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#
# N = int(input())
# bamboo = [list(map(int, input().split())) for _ in range(N)]
#
# 현재 위치에 도착했을때 가장 먼 이동거리 저장
# dp = [[1] * N for _ in range(N)]
#
# # 값 기준 오름차순 정렬
# cells = [(bamboo[i][j], i, j) for i in range(N) for j in range(N)]
# cells.sort()
#
# for val, r, c in cells:
#     cur = dp[r][c]
#     for dr, dc in delta:
#         nr, nc = r + dr, c + dc
#
#         # 이동방향이 인덱스 범위 안이고, 대나무가 더 많으면
#         # 이동방향 dp에 현재값 +1과 이동방향의 기존 값 비교 후 큰 값 저장
#         if 0 <= nr < N and 0 <= nc < N and bamboo[nr][nc] > val:
#             dp[nr][nc] = max(dp[nr][nc], cur + 1)
#
# print(max(map(max, dp)))


# 최초 풀이
# delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
#
# N = int(input())
#
# bamboo = [list(map(int, input().split())) for _ in range(N)]
#
# 현재 위치에서 가장 멀리 이동가능한 거리 저장
# dp = [[0] * N for _ in range(N)]
#
# def dfs(r, c):
#     # 이동한적 있으면 저장 된 값 반환
#     if dp[r][c]:
#         return dp[r][c]
#
#     # 출발 시 이동 거리 1
#     dp[r][c] = 1
#
#     for dr, dc in delta:
#         nr = r + dr
#         nc = c + dc
#
#         # 인덱스 범위 밖이면 다른 방향 탐색
#         if nr < 0 or nr >= N or nc < 0 or nc >= N:
#             continue
#
#         # 이동방향의 대나무가 더 많으면
#         # 현재 이동거리와 이동방향의 최대 이동거리 +1 중 큰 값 저장
#         if bamboo[nr][nc] > bamboo[r][c]:
#             dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)
#
#     # 이동거리 반환
#     return dp[r][c]
#
# for i in range(N):
#     for j in range(N):
#         dfs(i, j)
#
# answer = 0
# for x in range(N):
#     answer = max(answer, *dp[x])
#
# print(answer)