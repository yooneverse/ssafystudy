'''
포도주 잔 일렬

1. 선택하면 다 마시고 제자리
2. 붙어있는 3개 연속 모두 마실 수 없음 -> 최대 2개까지

-> 가장 많은 양 먹기 -> dp
'''

n = int(input()) # 포도주 잔의 개수
grape = [int(input()) for _ in range(n)]

dp = [0] * (n+1)

# 초기 값
dp[1] = grape[0]
if n >= 2:
    dp[2] = grape[0] + grape[1]

# i 번째 잔에서 가능한 경우
for i in range(3, n+1):
    dp[i] = max(
    # 1. - - X
    dp[i-1], 

    # 2. - X O
    dp[i-2] + grape[i-1],

    # 3. X O O
    dp[i-3] + grape[i-2] + grape[i-1]
    )
    
print(dp[n])

    