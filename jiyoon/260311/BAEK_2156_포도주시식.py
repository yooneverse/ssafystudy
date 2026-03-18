import sys
input = sys.stdin.readline  # 입력 속도 향상을 위한 설정

n = int(input())  # 포도주 잔의 개수 입력

wine = [0]  # 1번 인덱스부터 사용하기 위해 더미 값 추가 (wine[1]부터 사용)

# 각 포도주 잔의 양 입력
for _ in range(n):
    wine.append(int(input()))

# 잔이 1개일 때는 그냥 그 잔을 마시면 최대
if n == 1:
    print(wine[1])

# 잔이 2개일 때는 두 잔 모두 마시는 것이 최대
elif n == 2:
    print(wine[1] + wine[2])

else:
    # dp[i] = i번째 잔까지 고려했을 때 마실 수 있는 최대 포도주 양
    dp = [0] * (n + 1)

    # 첫 번째 잔까지의 최대
    dp[1] = wine[1]

    # 두 번째 잔까지의 최대 (1,2번 둘 다 마시는 것이 최대)
    dp[2] = wine[1] + wine[2]

    # 세 번째 잔부터는 규칙을 고려해 계산
    for i in range(3, n + 1):
        dp[i] = max(
            dp[i - 1],                      # ① i번째 잔을 안 마시는 경우
                                            # → i-1까지의 최대값 그대로

            dp[i - 2] + wine[i],            # ② i번째 잔만 마시는 경우
                                            # → i-1은 건너뛰고 i를 마심

            dp[i - 3] + wine[i - 1] + wine[i]  # ③ i-1, i번째 잔을 연속으로 마시는 경우
                                              # → 대신 i-2는 마시면 안 됨
        )

    # 마지막 잔까지 고려했을 때의 최대값 출력
    print(dp[n])