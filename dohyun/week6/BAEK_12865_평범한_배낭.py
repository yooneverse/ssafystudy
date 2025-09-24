# BAEK 12865. 평범한 배낭
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
dp = [0] * (K + 1)  # 가치 저장할 dp 1차원 배열 생성
for i in range(N):
    # 무게와 가치를 반복하여 입력받음
    W, V = map(int, input().split())
    #
    for w in range(K, W - 1, -1):
        dp[w] = max(dp[w], dp[w - W] + V)

print(max(dp))
