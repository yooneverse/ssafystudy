# 출결사항이 기록되는 출결은 출석, 지각, 결석이다.
# 개근상을 받을 수 없는 사람은 지각을 두 번 이상 했거나, 결석을 세 번 연속으로 한 사람이다.
# O를 출석, L을 지각, A를 결석

N = int(input())
MOD = 1_000_000

# dp[day][late][absent]
dp = [[[0] * 3 for _ in range(2)] for _ in range(N + 1)]
dp[0][0][0] = 1

for day in range(N):
    for late in range(2):
        for absent in range(3):
            cur = dp[day][late][absent]
            if cur == 0:
                continue

            # 1) 출석(O)
            dp[day + 1][late][0] = (dp[day + 1][late][0] + cur) % MOD

            # 2) 지각(L) - 지각은 최대 1번
            if late == 0:
                dp[day + 1][1][0] = (dp[day + 1][1][0] + cur) % MOD

            # 3) 결석(A) - 연속 결석 최대 2번
            if absent < 2:
                dp[day + 1][late][absent + 1] = (
                    dp[day + 1][late][absent + 1] + cur
                ) % MOD

# 결과 합산
answer = 0
for late in range(2):
    for absent in range(3):
        answer = (answer + dp[N][late][absent]) % MOD

print(answer)


