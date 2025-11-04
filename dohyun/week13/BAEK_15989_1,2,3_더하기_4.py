# BAEK 15989. 1, 2, 3 더하기 4
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    n = int(input())
    # dp 생성
    dp = [0] * (n + 1)
    # 공집합 개념의 dp[0]
    dp[0] = 1
    # 1 부터 3 까지 하니씩 사용
    for j in range(1, 4):
        # 루프마다 1, 2, 3 을 추가한 갯수 더해짐
        for i in range(1, n + 1):
            if i - j >= 0:
                dp[i] += dp[i - j]

    print(dp[n])
