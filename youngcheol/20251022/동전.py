T = int(input())
for _ in range(1, T+1):
    N = int(input())  # N은 동전의 개수
    num = map(int, input().split()) # 동전의 액면가들

    price = int(input())   #목표금액

    dp = [0] * (price+1)
    dp[0] = 1

    # 조합만 세기 위한 전형적인 코인 체인지 1차원 DP
    # 바깥 루프: 동전, 안쪽 루프: 금액(오름차순)
    # 이렇게 해야 1+2와 2+1 같은 순서만 다른 경우가 한 번만 카운트됨
    for c in num:
        for a in range(c, price+1):
            dp[a] += dp[a-c]
            # '마지막에 동전 c를 하나 더 썼다'고 보면, 직전 금액은 a-c
            # a-c를 만드는 모든 방법 수(dp[a-c])를 현재 dp[a]에 더해 누적

    print(dp[price])