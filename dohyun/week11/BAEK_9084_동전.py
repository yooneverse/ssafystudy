# BAEK 9084. 동전
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))   # N 개 코인 리스트
    M = int(input())    # 목표값

    # dp 설정
    dp = [0] * (M + 1)
    # 동전을 0개 써서 0원을 만드는 법 한 가지(부분집합 개념)
    dp[0] = 1

    # 동전을 꺼내 이전 dp 값에 동전의 크기만큼 넘어가며 더해줌
    # ex) 동전: 1, 2 / 목표값: 1000
    for coin in arr:
        # i) 1원
        # dp[1] = dp[1] + dp[0] = 0 + 1 (1원을 만드려면 1원 동전 하나가 있어야 함)
        # dp[2] = dp[2] + dp[1] = 0 + 1 (1 + 1)
        # ...
        # dp[1000] = dp[1000] + dp[999] = 0 + 1 (1 + 1 + ... + 1 = 1000)
        # ii) 2원
        # dp[2] = dp[2] + dp[0] = 1 + 1 (2원을 만드려면 1 + 1 / 2)
        # dp[3] = dp[3] + dp[1] = 1 + 1 (1 + 1 + 1 / 1 + 2)
        # dp[4] = dp[4] + dp[2] = 1 + 2 (1 + 1 + 1 + 1 / 1 + 1 + 2 / 2 + 2)
        # ...
        for i in range(coin, M + 1):
            dp[i] += dp[i - coin]

    print(dp[M])