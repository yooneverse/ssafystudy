#  https://www.acmicpc.net/problem/12865
# GPT없이 DP 풀어보고싶다...

N, M = map(int, input().split())  # N: 아이템 개수, M: 최대 무게
items = [tuple(map(int, input().split())) for _ in range(N)]  # 각 아이템의 (무게, 가치)

dp = [0] * (M + 1)  # dp[c] = 현재 배낭 용량이 c일 때 얻을 수 있는 최대 가치

# 모든 아이템을 하나씩 고려
for weight, value in items:
    # 뒤에서 앞으로(cap ↓) 갱신해야 같은 아이템 중복 선택을 방지 할 수 있음
    for cap in range(M, weight - 1, -1):
        # 만약 이번 아이템을 넣었을 때 더 가치가 크다면 갱신
        if dp[cap - weight] + value > dp[cap]:
            dp[cap] = dp[cap - weight] + value
            # print(dp)  # 디버깅용: 현재 dp 배열 상태 출력

# 최종 답은 용량 M에서 얻을 수 있는 최대 가치
# 항상 최대 가치는 배열의 맨 끝임
print(dp[M])

"""
input
4 7
6 13
4 8
3 6
5 12
---------
output
[0, 0, 0, 0, 0, 0, 0, 13]
[0, 0, 0, 0, 0, 0, 13, 13]
[0, 0, 0, 0, 0, 8, 13, 13]
[0, 0, 0, 0, 8, 8, 13, 13]
[0, 0, 0, 0, 8, 8, 13, 14]
[0, 0, 0, 6, 8, 8, 13, 14]
[0, 0, 0, 6, 8, 12, 13, 14]
"""
