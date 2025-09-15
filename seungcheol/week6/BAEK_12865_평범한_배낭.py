# 최초 풀이
# N, K = map(int, input().split())
#
# backpack = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
#
#
# dp = [[0] * (K + 1) for _ in range(N + 1)]
#
# for i in range(1, N + 1):
#     # 가방에 j이하의 무게만 담을 수 있다.
#     for j in range(1, K + 1):
#         # 현재 물건이 배낭의 무게제한 j보다 무거우면
#         # 이전 물건(i - 1)까지의 j무게 칸의 정보를 저장
#         if j < backpack[i][0]:
#             dp[i][j] = dp[i - 1][j]
#         # 현재 물건이 배낭의 무게제한 j과 같거나 보다 가벼우면
#         # 이전 물건(i - 1)까지의 j무게 칸의 정보와
#         # 현재 물건 만족도 + 이전물건 까지의 j-현재무게 칸의 정보를 비교 후 저장
#         elif j >= backpack[i][0]:
#             dp[i][j] = max(dp[i - 1][j], backpack[i][1] + dp[i - 1][j - backpack[i][0]])
#
# print(dp[N][K])

# gpt 풀이
import sys
# 버퍼에 입력값 int 타입으로 저장
it = map(int, sys.stdin.buffer.read().split())

# it값 하나씩 할당
N, K = next(it), next(it)

# 제한 무게 +1만큼 dp 생성
dp = [0] * (K + 1)

# 물건 수 만큼 반복
for _ in range(N):
    # it값 하나씩 할당
    w, v = next(it), next(it)

    for i in range(K, w - 1, -1):
        cand = v + dp[i - w]

        if cand > dp[i]:
            dp[i] = cand

print(dp[K])
